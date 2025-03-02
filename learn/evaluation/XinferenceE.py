import requests
from langchain.embeddings.base import Embeddings

import openai

# Assume that the model is already launched.
# The api_key can't be empty, any string is OK.
client = openai.Client(api_key="not empty", base_url="http://192.168.136.31:9997/v1")
result = client.embeddings.create(model="bce-embedding-base_v1", input=["What is the capital of China?"])

if __name__ == "__main__":
    print(result)
