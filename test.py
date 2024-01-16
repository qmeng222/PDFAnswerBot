from langchain.prompts import ChatPromptTemplate # prompt
from langchain.chat_models import ChatOpenAI # model
from langchain.chains import LLMChain
from langchain.callbacks.base import BaseCallbackHandler
from dotenv import load_dotenv # for loading variables

load_dotenv() # load environment variables from .env

# `StreamingHandler`` inherits behavior from `BaseCallbackHandler`:
class StreamingHandler(BaseCallbackHandler):
    # define a callback method called `on_llm_new_token` which takes a token as an argument and prints it:
    def on_llm_new_token(self, token, **kwargs): # **kwargs indicates that it can accept additional keyword arguments (although they might not be used in this snippet)
        # print(token)
        pass

# create an instance of the ChatOpenAI class:
chat = ChatOpenAI(
   streaming=True, # control how OpenAI responds to LangChain
   callbacks=[StreamingHandler()]
)

# create a template (this type of template is specifically designed for creating conversations) that consists of a single message from the "human" role:
prompt = ChatPromptTemplate.from_messages([ # a list of tuples
    ("human", "{content}") # {content} placeholder
])

# define a class called StreamingChain that extends/inherits from LLMChain (inherits functionality from the LLMChain class):
class StreamingChain(LLMChain):
    # define a `stream` method to return a generator (a generator function produces values one at a time using the yield keyword):
    def stream(self, input): # `self` refers to the instance of the class
        print("🌈", self(input)) # the res of calling the chain
        yield 'hi'
        yield 'there'
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
