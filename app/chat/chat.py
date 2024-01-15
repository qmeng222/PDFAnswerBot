from app.chat.models import ChatArgs
from app.chat.vector_stores.pinecone import build_retriever # import func from the pinecone.py file

def build_chat(chat_args: ChatArgs):
    """
    :param chat_args: ChatArgs object containing conversation_id, pdf_id, metadata, and streaming flag.
    :return: A chain

    Example Usage:
        chain = build_chat(chat_args)
    """
    retriever = build_retriever(chat_args)
