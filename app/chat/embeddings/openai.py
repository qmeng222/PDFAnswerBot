# import os
# from dotenv import load_dotenv
from dotenv import dotenv_values
from langchain.embeddings import OpenAIEmbeddings

# load_dotenv()  # take environment variables from .env

# # retrieve OPENAI_API_KEY from the .env file:
# key = os.environ.get('OPENAI_API_KEY')
config = dotenv_values(".env")
k = config["OPENAI_API_KEY"]
# print("🔑", k)

# create OpenAI embeddings:
embeddings = OpenAIEmbeddings(openai_api_key=k)
