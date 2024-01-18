from langchain.chains import ConversationalRetrievalChain
from app.chat.chains.streamable import StreamableChain # import the mixin that I created

# extend StreamableChain and ConversationalRetrievalChain:
class StreamingConversationalRetrievalChain(
    StreamableChain, ConversationalRetrievalChain
):
    pass
