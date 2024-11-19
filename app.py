import requests
from openai import OpenAI
import os
import hashlib
from dotenv import load_dotenv

load_dotenv()
def create(name):
    response = requests.put(url=url, json=vectors)
    return response

def add(name):
    response = requests.put(url=url, json=vectors)
    return response

def embed(input):
    response = client.embeddings.create(
        input=input,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
url = 'http://localhost:6333/collections/wiedza'
vectors = {"vectors": {"size": 1536,"distance": "Cosine"}}
with open('baza.txt', 'r', encoding='utf-8') as plik:
    # Wczytaj linie do listy
    linie = plik.readlines()


linie = [linia.strip() for linia in linie]

# for i in linie:
#     json = {"points": [{'id': hashlib.md5(i.encode()).hexdigest(), "payload":{'text': i}, "vector": embed(i)}]}
     
#     print(json)
#     r = requests.put(url=f'http://localhost:6333/collections/wiedza/points', json=json)
#     print(r)
pytanie = embed("jak ma na imie pies Adama?")
q_json = {"vector": pytanie,"limit": 1,"with_payload": True}
q = requests.post(url=f'{url}/points/search', json=q_json)
print(q.text)
