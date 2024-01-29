# import os
from dotenv import dotenv_values
from langfuse.client import Langfuse

config = dotenv_values(".env") # return a dict with the values parsed from the .env file
# a = config["LANGFUSE_PUBLIC_KEY"]
# b = config["LANGFUSE_SECRET_KEY"]
# print("👀", a, type(a))
# print("👀", b, type(b))

# create a Langfuse client:
langfuse = Langfuse(
    # os.environ["LANGFUSE_PUBLIC_KEY"],
    # os.environ["LANGFUSE_SECRET_KEY"],
    public_key=config["LANGFUSE_PUBLIC_KEY"],
    secret_key=config["LANGFUSE_SECRET_KEY"],
    host="https://prod-langfuse.fly.dev"
)
