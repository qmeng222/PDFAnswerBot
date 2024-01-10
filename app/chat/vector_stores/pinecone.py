import os
import pinecone
from langchain.vectorstores import Pinecone
from app.chat.embeddings.openai import embeddings # import OpenAI embeddings object from app/chat/embeddings/openai.py file

# initialize Pinecone client:
pinecone.init(
  api_key=os.getenv("PINECONE_API_KEY"),
  environment=os.getenv("PINECONE_ENV_NAME")
)

# create vector store (for storing docs):
vector_store = Pinecone.from_existing_index(
  # 1st arg: pinecone index name, 2nd arg: embeddings obj that already imported
  os.getenv("PINECONE_INDEX_NAME"), embeddings
)

# # one feature shared by various vector stores, such as Chroma and Pinecone, is the capability to transform them into retrievers
# # build a retriever out of the vector store:
# vector_store.as_retriever()
