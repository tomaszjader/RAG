from openai import OpenAI
from dotenv import load_dotenv
import os
from app import generate_answer_with_context

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

query = "W raporcie, z którego dnia znajduje się wzmianka o kradzieży prototypu broni?"
context = "W raporcie z dnia 12 stycznia 2024 roku odnotowano kradzież prototypu broni."

print("Testing generation with hardcoded context...")
answer = generate_answer_with_context(client, query, context)
print(f"Query: {query}")
print(f"Context: {context}")
print(f"Generated Answer: {answer}")
