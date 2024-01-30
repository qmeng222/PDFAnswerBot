from langfuse.model import CreateTrace
from app.chat.tracing.langfuse import langfuse

# define a basic traceable chain mixin:
class TraceableChain:
    def __call__(self, *args, **kwargs):
        # print("👋", self.metadata) # {'conversation_id': '...', 'user_id': '...', 'pdf_id': '...'}

        # initiate a trace within Langfuse's observability system:
        trace = langfuse.trace(
            CreateTrace(
                id=self.metadata["conversation_id"],
                metadata=self.metadata
            )
        )
        callbacks = kwargs.get("callbacks", [])
        callbacks.append(trace.getNewHandler())
        kwargs["callbacks"] = callbacks # reassign the list of callbacks back to the keyword arguments

        return super().__call__(*args, **kwargs)
