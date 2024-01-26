import os # for interacting with the operating system (reading or writing to the file system, manipulating paths, working with environment variables, ...)
import redis # for interacting with the Redis in-memory data structure store (store and retrieve data in a key-value format)

# create a Redis client by connecting to a Redis server:
client = redis.Redis.from_url(
  os.environ["REDIS_URI"], # specify the Redis server connection details
  decode_responses=True # responses from Redis are decoded from bytes (a sequence of binary data) to strings
)
