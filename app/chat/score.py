from app.chat.redis import client # import Redis client from the redis.py file


def random_component_by_score(component_type, component_map):
    # make sure the `component_type` is 'llm', 'retriever', or 'memory':
    if component_type not in ["llm", "retriever", "memory"]:
        raise ValueError("Invalid component_type")

    print("1️⃣", component_type)

    # (from Redis) get all k-v pairs of the hash containing the score total for the given commponent_type:
    # hash name: llm/retriever/memory_score_values
    values = client.hgetall(f"{component_type}_score_values") # `values` is a dict
    # (from Redis) get all k-v pairs of the hash containing the score count for the given component_type:
    counts = client.hgetall(f"{component_type}_score_counts") # `counts` is a dict

    print("2️⃣", values, counts) # the values of the dict are in string type

    # get all the valid component names from the component map:

    # loop over those valid names and use them to calculate the average score for each & add average score to a dictionary:

    # do a weighted random selection:


def score_conversation(
    conversation_id: str, score: float, llm: str, retriever: str, memory: str
) -> None:
    score = min(max(score, 0), 1) # at least 0 & at most 1

    # (hash increment by) increment the value of a field (llm) within a Redis hash:
    # (the name of the Redis hash, the field within the hash whose value you want to increment, the value associated with the field in the hash will be incremented)
    client.hincrby("llm_score_values", llm, score)
    client.hincrby("llm_score_counts", llm, 1)

    client.hincrby("retriever_score_values", retriever, score)
    client.hincrby("retriever_score_counts", retriever, 1)

    client.hincrby("memory_score_values", memory, score)
    client.hincrby("memory_score_counts", memory, 1)


def get_scores():
    """
    Retrieves and organizes scores from the langfuse client for different component types and names.
    The scores are categorized and aggregated in a nested dictionary format where the outer key represents
    the component type and the inner key represents the component name, with each score listed in an array.

    The function accesses the langfuse client's score endpoint to obtain scores.
    If the score name cannot be parsed into JSON, it is skipped.

    :return: A dictionary organized by component type and name, containing arrays of scores.

    Example:

        {
            'llm': {
                'chatopenai-3.5-turbo': [score1, score2],
                'chatopenai-4': [score3, score4]
            },
            'retriever': { 'pinecone_store': [score5, score6] },
            'memory': { 'persist_memory': [score7, score8] }
        }
    """

    pass
