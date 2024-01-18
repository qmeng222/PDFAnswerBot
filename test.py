from langchain.prompts import ChatPromptTemplate # prompt
from langchain.chat_models import ChatOpenAI # model
from langchain.chains import LLMChain
from langchain.callbacks.base import BaseCallbackHandler
from queue import Queue # from the queue module import the Queue class
from threading import Thread # for managing multithreads (multiple threads run concurrently within a single program, allowing for parallel execution of tasks)
from dotenv import load_dotenv # for loading variables


load_dotenv() # load environment variables from .env

# ------ queue ------
# create an instance of the Queue (FIFO) class:
queue = Queue()


# ------ streaming handler ------
class StreamingHandler(BaseCallbackHandler): # `StreamingHandler` inherits behavior from `BaseCallbackHandler`
    # define a callback method called `on_llm_new_token` which takes a token as an argument and prints it:
    def on_llm_new_token(self, token, **kwargs):
        # print(token)
        queue.put(token)


    # two scenarios to end the while loop:

    # 1. callback method to notify the end of the generated response:
    def on_llm_end(self, response, **kwargs):
        queue.put(None) # add None to the queue

    # 2. callback method to handle errors during response generation (eg: API key is invalid, ...)
    def on_llm_error(self, error, **kwargs):
        queue.put(None) # add None to the queue as well


# ------ model ------
# create an instance of the ChatOpenAI class:
chat = ChatOpenAI(
   streaming=True, # control how OpenAI responds to LangChain
   callbacks=[StreamingHandler()]
)


# ------ prompt ------
# create a template (this type of template is specifically designed for creating conversations) that consists of a single message from the "human" role:
prompt = ChatPromptTemplate.from_messages([ # a list of tuples
    ("human", "{content}") # {content} placeholder
])


# ------ streaming chain ------
class StreamingChain(LLMChain): # inherit functionality from the LLMChain class
    # define a `stream` method to return a generator (a generator function produces values one at a time using the yield keyword):
    def stream(self, input): # `self` refers to the instance of the class
        # define a `task`` func separately:
        def task():
            self(input) # run the chain

        # (in the main stream) when `thread.start()` is called, the `task` func runs concurrently:
        Thread(target=task).start()

        # in the main stream:
        while True:
            token = queue.get() # just wait if the queue is empty
            if token is None: # end of response
                break
            yield token # generate one word token at a time
# now any instance of the StreamingChain class has a `stream` method

chain = StreamingChain(llm=chat, prompt=prompt) # an instance of the StreamingChain class

# the `chain` obj has the `stream` method:
for output in chain.stream(input={"content": "tell me a joke"}):
    print(output)

# chain = LLMChain(llm=chat, prompt=prompt)

# # NOTE: LLMs are happy to stream, but chains are not!
# output = chain.stream(input={"content": "Tell me a joke."})
# # print("✅", output)
# for msg in output:
#   print("👋", msg)

# # use the template to create an actual conversation by filling in the {content} placeholder with the specific content (format the template):
# messages = prompt.format_messages(content="Tell me a joke.")
# # 👆 the resulting messages variable contains a formatted conversation ready to be used as input for a language model

# # check the output:
# output = chat(messages)
# print("👀", output)

# # examine the process of streaming the response from OpenAI to LangChain & from LangChain to the user:
# output = chat.stream(messages) # a generator obj
# # print("👀", output)
# for message in output:
#     print(message.content)
