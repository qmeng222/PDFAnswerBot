from flask import current_app
from queue import Queue # from the queue module import the Queue class
from threading import Thread # for managing multithreads (multiple threads run concurrently within a single program, allowing for parallel execution of tasks)
from app.chat.callbacks.stream import StreamingHandler # import from file


# ------ streaming chain ------
# # 1. inheritance approach:
# class StreamingChain(LLMChain): # inherit functionality from the LLMChain class
# # define a `stream` method to return a generator (a generator function produces values one at a time using the yield keyword):
# 2. Mixin approach: mix in or add functionality to a class without using traditional inheritance:
class StreamableChain:
    def stream(self, input): # `self` refers to the instance of the class
        # create a queue and handler for every single user/call:
        queue = Queue()
        handler = StreamingHandler(queue) # an instance of StreamingHandler is created with queue as an argument

        # define a `task`` func separately:
        def task(app_context):
            app_context.push()
            self(input, callbacks=[handler]) # run the chain

        # (in the main stream) when `thread.start()` is called, the `task` func runs concurrently:
        # Thread(target=task).start()
        Thread(target=task, args=[current_app.app_context()]).start()

        # in the main stream:
        while True:
            token = queue.get() # just wait if the queue is empty
            if token is None: # end of response
                break
            yield token # generate one word token at a time
# now any instance of the StreamingChain class has a `stream` method
