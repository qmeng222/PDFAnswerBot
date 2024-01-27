from pydantic import BaseModel
from langchain.schema import BaseChatMessageHistory
from app.web.api import (
    get_messages_by_conversation_id,
    add_message_to_conversation
) # import from file

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
