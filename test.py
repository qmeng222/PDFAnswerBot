# print("hi there👋")

from langchain.prompts import ChatPromptTemplate # prompt
from langchain.chat_models import ChatOpenAI # model
from dotenv import load_dotenv # for loading variables

load_dotenv() # load environment variables from .env

chat = ChatOpenAI() # create an instance of the ChatOpenAI class

# create a template (this type of template is specifically designed for creating conversations) that consists of a single message from the "human" role:
prompt = ChatPromptTemplate.from_messages([ # a list of tuples
    ("human", "{content}") # {content} placeholder
])
# use the template to create an actual conversation by filling in the {content} placeholder with the specific content (format the template):
messages = prompt.format_messages(content="Tell me a joke")
# 👆 the resulting messages variable contains a formatted conversation ready to be used as input for a language model

output = chat(messages)
print("👀", output)
