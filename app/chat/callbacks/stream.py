from langchain.callbacks.base import BaseCallbackHandler


# ------ streaming handler ------
class StreamingHandler(BaseCallbackHandler): # `StreamingHandler` inherits behavior from `BaseCallbackHandler`
    # init func to receive the queue and assign it to an instance variable:
    def __init__(self, queue):
        self.queue = queue
        self.streaming_run_ids = set()

    def on_chat_model_start(self, serialized, messages, run_id, **kwargs):
        # print("1️⃣", serialized)
        # print("2️⃣", run_id)
        # streaming handler only listens to events coming from models with streaming=True:
        if serialized["kwargs"]["streaming"]: # if True
            self.streaming_run_ids.add(run_id)

    # define a callback method that takes a token and puts it into the queue:
    def on_llm_new_token(self, token, **kwargs):
        # print(token)
        self.queue.put(token)

    # two scenarios to end the while loop:
    # 1. callback method to notify the end of the generated response:
    def on_llm_end(self, response, run_id, **kwargs):
        # if run_id is present in the set:
        if run_id in self.streaming_run_ids:
            self.queue.put(None) # add None to the queue
            self.streaming_run_ids.remove(run_id) # remove from set (not needed anymore)

    # 2. callback method to handle errors during response generation (eg: API key is invalid, ...)
    def on_llm_error(self, error, **kwargs):
        self.queue.put(None) # add None to the queue as well
