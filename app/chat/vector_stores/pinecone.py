import os
# from dotenv import load_dotenv
from dotenv import dotenv_values
import pinecone
from langchain.vectorstores import Pinecone
from app.chat.embeddings.openai import embeddings # import OpenAI embeddings object from app/chat/embeddings/openai.py file

# load_dotenv()  # take environment variables from .env

config = dotenv_values(".env") # return a dict with the values parsed from the .env file
# print("👻", config)
# a = config["OPENAI_API_KEY"]
# b = config["PINECONE_API_KEY"]
# c = config["PINECONE_INDEX_NAME"]
# print("1️⃣", a, type(a))
# print("2️⃣", b, type(b))
# print("3️⃣", c, type(c))

# initialize Pinecone client:
pinecone.init(
  # api_key=os.getenv("PINECONE_API_KEY"),
  # environment=os.getenv("PINECONE_ENV_NAME")
  api_key=config["PINECONE_API_KEY"],
  environment=config["PINECONE_ENV_NAME"]
)

# create vector store (for storing docs):
vector_store = Pinecone.from_existing_index(
  # 1st arg: pinecone index name, 2nd arg: embeddings obj that already imported
  # os.getenv("PINECONE_INDEX_NAME"), embeddings
  config["PINECONE_INDEX_NAME"], embeddings
)

# # one feature shared by various vector stores, such as Chroma and Pinecone, is the capability to transform them into retrievers
# # build a retriever out of the vector store:
# vector_store.as_retriever()
def build_retriever(chat_args, k):
    search_kwargs = {
        "filter": { "pdf_id": chat_args.pdf_id },
        "k": k
    }
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )
