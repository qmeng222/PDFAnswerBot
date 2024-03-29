# import the partial function from the functools module:
from functools import partial

# (relative) import the build_llm function from the chatopenai.py file:
from .chatopenai import build_llm

# llm component map:
llm_map = {
    "gpt-4": partial(build_llm, model_name="gpt-4"),
    "gpt-3.5-turbo": partial(build_llm, model_name="gpt-3.5-turbo")
}
