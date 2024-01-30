import random
from langchain.chat_models import ChatOpenAI
from app.chat.models import ChatArgs

# from app.chat.llms.chatopenai import build_llm # model
# from app.chat.memories.sql_memory import build_memory # memory
# from app.chat.vector_stores.pinecone import build_retriever # import func from the pinecone.py file
from app.chat.llms import llm_map
from app.chat.memories import memory_map
from app.chat.vector_stores import retriever_map

from app.chat.chains.retrieval import StreamingConversationalRetrievalChain # chain
from app.web.api import ( # from api.py file
    set_conversation_components,
    get_conversation_components
)
from app.chat.score import random_component_by_score # for picking the best rated chain components
# from app.chat.tracing.langfuse import langfuse # import the langfuse client from the flanfuse.py file
# from langfuse.model import CreateTrace # import the class from the langfuse.model module for creating a trace object (which captures detailed logs of prompts, actions, outputs and feedback)

# select a combination of chain components with high ratings using weighted random selection:
def select_component(
    component_type,
    component_map,
    chat_args
):
    components = get_conversation_components(
        chat_args.conversation_id
    ) # a dictionary
    previous_component = components[component_type]

    if previous_component:
        # if this is NOT the first message of the conversation, I'll use the same builder again:
        builder = component_map[previous_component]
        return previous_component, builder(chat_args)
    else: # otherwise, this is the first message of the conversation, and I will do do a weighted random selection to pick the combination to use:
        random_name = random_component_by_score(component_type, component_map)
        builder = component_map[random_name]
        return random_name, builder(chat_args)

def build_chat(chat_args: ChatArgs):
    # name of the retriever, the actual retriever:
    retriever_name, retriever = select_component(
        "retriever", # component_type
        retriever_map, # component_map
        chat_args
    )
    llm_name, llm = select_component(
        "llm",
        llm_map,
        chat_args
    )
    memory_name, memory = select_component(
        "memory",
        memory_map,
        chat_args
    )

    # print(
    #     f"Running chain with:\n🧠memory: {memory_name},\n🤖llm: {llm_name},\n🥡retriever: {retriever_name}"
    # )

    # set conversation components:
    set_conversation_components(
        chat_args.conversation_id,
        llm=llm_name,
        retriever=retriever_name,
        memory=memory_name
    )

    condense_question_llm = ChatOpenAI(streaming=False)

    return StreamingConversationalRetrievalChain.from_llm(
        llm=llm,
        condense_question_llm=condense_question_llm,
        memory=memory,
        retriever=retriever,
        # callbacks=[trace.getNewHandler()]
        metadata=chat_args.metadata
    )

    """
    :param chat_args: ChatArgs object containing conversation_id, pdf_id, metadata, and streaming flag.
    :return: A chain

    Example Usage:
        chain = build_chat(chat_args)
    """
    # llm = build_llm(chat_args)
    # memory = build_memory(chat_args)
    # retriever = build_retriever(chat_args)
    # condense_question_llm = ChatOpenAI(streaming=False) # False by default

    # return StreamingConversationalRetrievalChain.from_llm(
    #     llm=llm,
    #     condense_question_llm=condense_question_llm,
    #     memory=memory,
    #     retriever=retriever
    # )
