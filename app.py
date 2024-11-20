import requests
from openai import OpenAI
import os
import hashlib
from dotenv import load_dotenv

load_dotenv()

def create(url, json):
    response = requests.put(url=url, json=json)
    return response.text

def add(url, json):
    response = requests.put(url=f"{url}/points", json=json)
    return response.text

def embed(input):
    response = client.embeddings.create(
        input=input,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

def indexing(linie, url):
    for i in linie:
        json = {"points": [{'id': hashlib.md5(i.encode()).hexdigest(), "payload":{'text': i}, "vector": embed(i)}]}
        r = add(url=url, json=json)
    return

def search(url, query):
    json = {"vector": embed(query),"limit": 1,"with_payload": True}
    response = requests.post(url=f'{url}/points/search', json=json)
    return response.text


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
url = 'http://localhost:6333/collections/wiedza'
vectors = {"vectors": {"size": 1536,"distance": "Cosine"}}
create(url, vectors)

with open('baza.txt', 'r', encoding='utf-8') as plik:
    linie = plik.readlines()


linie = [linia.strip() for linia in linie]
indexing(linie, url)

pytanie = "jak ma na imie pies Adamsia?"

print(search(url, pytanie))
