# This code defines a function that creates and returns an instance of the ChatOpenAI class from the langchain.chat_models module:

from langchain.chat_models import ChatOpenAI # import class

def build_llm(chat_args, model_name): # take in an obj containing info related to a chat
    # return the newly created instance of the ChatOpenAI class:
    return ChatOpenAI(
        streaming=chat_args.streaming,
        model_name=model_name # gpt-3.5-turbo if not specified
    )
