from langchain.memory import ConversationBufferWindowMemory
from app.chat.memories.histories.sql_history import SqlMessageHistory

def window_buffer_memory_builder(chat_args):
    return ConversationBufferWindowMemory(
        memory_key="chat_history", # for later retrieval or updating
        output_key="answer", # for accessing the output
        return_messages=True, # retrieve the entire set of msgs stored in history
        chat_memory=SqlMessageHistory(
            conversation_id=chat_args.conversation_id
        ),
        k=2 # only store the last k conversation exchanges
    )
