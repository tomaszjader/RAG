import requests
from openai import OpenAI
import os
import hashlib
from dotenv import load_dotenv


load_dotenv()


def create_collection(url, collection_config):
    response = requests.put(url=url, json=collection_config)
    if response.status_code == 200:
        print("Kolekcja została utworzona pomyślnie.")
    else:
        print(f"Błąd tworzenia kolekcji: {response.text}")
    return response.text


def add_points(url, json_data):
    response = requests.put(url=f"{url}/points", json=json_data)
    if response.status_code == 200:
        print("Punkty zostały dodane pomyślnie.")
    else:
        print(f"Błąd dodawania punktów: {response.text}")
    return response.text


def generate_embedding(client, text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding


def index_data(lines, url, client):
    for line in lines:
        point_id = hashlib.md5(line.encode()).hexdigest()
        vector = generate_embedding(client, line)
        json_data = {
            "points": [
                {
                    'id': point_id,
                    "payload": {'text': line},
                    "vector": vector
                }
            ]
        }
        add_points(url=url, json_data=json_data)


def search_collection(url, query, client):
    query_vector = generate_embedding(client, query)
    search_payload = {
        "vector": query_vector,
        "limit": 1,
        "with_payload": True
    }
    response = requests.post(url=f'{url}/points/search', json=search_payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Błąd wyszukiwania: {response.text}")
        return None

def search_collection_with_context(url, query, client):
    query_vector = generate_embedding(client, query)
    search_payload = {
        "vector": query_vector,
        "limit": 3,  # Pobierz więcej wyników, aby zwiększyć kontekst
        "with_payload": True
    }
    response = requests.post(url=f'{url}/points/search', json=search_payload)
    if response.status_code == 200:
        results = response.json()
        context = "\n".join([result['payload']['text'] for result in results['result']])
        return context
    else:
        print(f"Błąd wyszukiwania: {response.text}")
        return None


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
collection_url = 'http://localhost:6333/collections/wiedza'


collection_config = {
    "vectors": {
        "size": 1536,
        "distance": "Cosine"
    }
}





with open('baza.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file.readlines()]

create_collection(collection_url, collection_config)
index_data(lines, collection_url, client)



query = "W raporcie, z którego dnia znajduje się wzmianka o kradzieży prototypu broni?"
context = search_collection_with_context(collection_url, query, client)

if context:
    # answer = generate_answer_with_context(client, query, context)
    answer = search_collection(collection_url, query, client)
    print("Odpowiedź z generacją:", answer)
else:
    print("Nie znaleziono odpowiedniego kontekstu.")
