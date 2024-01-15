# This code defines a function that creates and returns an instance of the ChatOpenAI class from the langchain.chat_models module:

from langchain.chat_models import ChatOpenAI # import class

def build_llm(chat_args): # take in an obj containing info related to a chat
    return ChatOpenAI() # return the newly created instance of the ChatOpenAI class
