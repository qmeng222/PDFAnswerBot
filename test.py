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
        print(token)

# create an instance of the ChatOpenAI class:
chat = ChatOpenAI(
   streaming=True, # control how OpenAI responds to LangChain
   callbacks=[StreamingHandler()]
)

# create a template (this type of template is specifically designed for creating conversations) that consists of a single message from the "human" role:
prompt = ChatPromptTemplate.from_messages([ # a list of tuples
    ("human", "{content}") # {content} placeholder
])

chain = LLMChain(llm=chat, prompt=prompt)

# NOTE: LLMs are happy to stream, but chains are not!
output = chain.stream(input={"content": "Tell me a joke."})
# print("✅", output)
for msg in output:
  print("👋", msg)

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
