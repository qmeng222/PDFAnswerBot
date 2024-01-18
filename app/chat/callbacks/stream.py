from langchain.callbacks.base import BaseCallbackHandler


# ------ streaming handler ------
class StreamingHandler(BaseCallbackHandler): # `StreamingHandler` inherits behavior from `BaseCallbackHandler`
    # init func to receive the queue and assign it to an instance variable:
    def __init__(self, queue):
        self.queue = queue

    # define a callback method that takes a token and puts it into the queue:
    def on_llm_new_token(self, token, **kwargs):
        # print(token)
        self.queue.put(token)

    # two scenarios to end the while loop:
    # 1. callback method to notify the end of the generated response:
    def on_llm_end(self, response, **kwargs):
        self.queue.put(None) # add None to the queue

    # 2. callback method to handle errors during response generation (eg: API key is invalid, ...)
    def on_llm_error(self, error, **kwargs):
        self.queue.put(None) # add None to the queue as well
