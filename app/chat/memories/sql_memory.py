from langchain.memory import ConversationBufferMemory # import class from module
from app.chat.memories.histories.sql_history import SqlMessageHistory # import class from file

def build_memory(chat_args): # chat_args is an obj containing info related to a conversation
    # return the initialized ConversationBufferMemory object (for storing conversation history):
    return ConversationBufferMemory(
        chat_memory=SqlMessageHistory( # an instance of SqlMessageHistory
            conversation_id=chat_args.conversation_id
        ),
        return_messages=True, # retrieve the entire set of msgs stored in history
        memory_key="chat_history", # for later retrieval or updating (refer to conversational_QA_chain.png)
        output_key="answer" # for accessing the output (refer to conversational_QA_chain.png)
    )
