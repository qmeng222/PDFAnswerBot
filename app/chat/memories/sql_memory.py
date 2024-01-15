from pydantic import BaseModel
from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseChatMessageHistory
from app.web.api import (
    get_messages_by_conversation_id,
    add_message_to_conversation
)

# extend BaseChatMessageHistory and pedantic BaseModel:
class SqlMessageHistory(BaseChatMessageHistory, BaseModel):
    conversation_id: str # the id for all conversations for a particular PDF

    @property
    # find all messages in db for a particular conversation_id:
    def messages(self):
        return get_messages_by_conversation_id(self.conversation_id)

    # add a message to the database:
    def add_message(self, message):
        return add_message_to_conversation(
            conversation_id=self.conversation_id,
            role=message.type,
            content=message.content
        )

    def clear(self):
        pass

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
