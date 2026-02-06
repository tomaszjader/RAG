from openai import OpenAI
from dotenv import load_dotenv
import os
from app import generate_answer_with_context, search_collection_with_context

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
collection_url = 'http://localhost:6333/collections/wiedza'

query = "Jak nazwa się asystent poranka?"
print("Searching for context in vector database...")
context = search_collection_with_context(collection_url, query, client)

if context:
    print(f"Query: {query}")
    print(f"Context found: {context}")
    answer = generate_answer_with_context(client, query, context)
    print(f"Generated Answer: {answer}")
else:
    print("No context found in logic.")
