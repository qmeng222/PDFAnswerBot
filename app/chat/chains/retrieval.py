from langchain.chains import ConversationalRetrievalChain
from app.chat.chains.streamable import StreamableChain # import the mixin that I created
from app.chat.chains.traceable import TraceableChain # improt mixin from traceable.py file

# extend the chain mixins:
class StreamingConversationalRetrievalChain(TraceableChain, StreamableChain, ConversationalRetrievalChain
):
    pass
