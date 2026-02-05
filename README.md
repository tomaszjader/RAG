# RAG

The application leverages the Retrieval-Augmented Generation (RAG) approach, integrating Quadratic technology for data management and the OpenAI API for generating natural language responses. The project allows users to upload and process documents, index information, and perform efficient database searches with intelligent AI assistance.

## Wymagania wstępne (Prerequisites)

*   Python 3.8 lub nowszy
*   Docker (do uruchomienia bazy wektorowej Qdrant)
*   Klucz API OpenAI

## Instalacja (Installation)

1.  **Sklonuj repozytorium** (jeśli jeszcze tego nie zrobiłeś):
    ```bash
    git clone <adres_repozytorium>
    cd RAG
    ```

2.  **Zainstaluj zależności**:
    Zaleca się użycie wirtualnego środowiska (np. venv).
    ```bash
    pip install -r requirements.txt
    ```

3.  **Konfiguracja zmiennych środowiskowych**:
    Skopiuj plik `.env.example` do pliku `.env` i uzupełnij swój klucz API.
    ```bash
    cp .env.example .env
    ```
    Edytuj plik `.env` i wpisz swój klucz OpenAI:
    ```
    OPENAI_API_KEY=sk-proj-TwojKluczApi...
    ```

## Uruchomienie (Running)

1.  **Uruchom Qdrant (Baza wektorowa)**:
    Użyj Dockera, aby uruchomić instancję Qdrant lokalnie.
    ```bash
    docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
    ```
    Upewnij się, że kontener działa i nasłuchuje na porcie 6333.

2.  **Uruchom aplikację**:
    ```bash
    python app.py
    ```

    Skrypt `app.py`:
    *   Utworzy kolekcję w Qdrant (jeśli nie istnieje).
    *   Załaduje dane z pliku `baza.txt`, wygeneruje dla nich osadzenia (embeddings) i zapisze w bazie.
    *   Wykona przykładowe zapytanie RAG ("W raporcie, z którego dnia znajduje się wzmianka o kradzieży prototypu broni?") i wyświetli odpowiedź wygenerowaną przez GPT-3.5.

## Testowanie

Możesz również uruchomić prosty test:
```bash
python test_rag.py
```
