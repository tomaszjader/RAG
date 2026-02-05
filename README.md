# RAG

The application leverages the Retrieval-Augmented Generation (RAG) approach, integrating Quadratic technology for data management and the OpenAI API for generating natural language responses. The project allows users to upload and process documents, index information, and perform efficient database searches with intelligent AI assistance.

## Wymagania wstępne (Prerequisites)

Zanim zaczniesz, upewnij się, że masz zainstalowane następujące narzędzia:

*   **Python**: Wersja 3.8 lub nowsza. [Pobierz Python](https://www.python.org/downloads/)
*   **Docker**: Niezbędny do uruchomienia bazy wektorowej Qdrant.
    *   **Windows/Mac**: Zainstaluj [Docker Desktop](https://www.docker.com/products/docker-desktop/).
    *   **Linux**: Zainstaluj Docker Engine zgodnie z instrukcją dla Twojej dystrybucji.

## Instalacja (Installation)

1.  **Sklonuj repozytorium** (jeśli jeszcze tego nie zrobiłeś):
    ```bash
    git clone <adres_repozytorium>
    cd RAG
    ```

2.  **Zainstaluj zależności Pythona**:
    Zaleca się użycie wirtualnego środowiska (np. `venv`), aby uniknąć konfliktów bibliotek.
    ```bash
    # Utworzenie wirtualnego środowiska (opcjonalnie)
    python -m venv venv
    
    # Aktywacja środowiska (Windows)
    .\venv\Scripts\activate
    # Aktywacja środowiska (Linux/Mac)
    source venv/bin/activate

    # Instalacja bibliotek
    pip install -r requirements.txt
    ```

3.  **Konfiguracja zmiennych środowiskowych**:
    Skopiuj plik `.env.example` do pliku `.env` i uzupełnij swój klucz API.
    ```bash
    cp .env.example .env
    # Na Windows (PowerShell) użyj: copy .env.example .env
    ```
    Edytuj plik `.env` i wpisz swój klucz OpenAI:
    ```
    OPENAI_API_KEY=sk-proj-TwojKluczApi...
    ```

## Uruchomienie Qdrant (Baza wektorowa)

Aplikacja wymaga działającej instancji bazy Qdrant. Użyjemy do tego Dockera.

1.  **Pobierz obraz Qdrant** (opcjonalne, `docker run` zrobi to automatycznie, ale warto wiedzieć):
    ```bash
    docker pull qdrant/qdrant
    ```

2.  **Uruchom kontener Qdrant**:
    Poniższa komenda uruchomi bazę danych i wystawi ją na porcie 6333.
    ```bash
    docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
    ```
    *   `-p 6333:6333`: Port HTTP interfejsu API.
    *   `-p 6334:6334`: Port gRPC (opcjonalny dla tego projektu, ale warto go mieć).
    
    PO URUCHOMIENIU: Nie zamykaj tego okna terminala. Baza musi działać w tle. Możesz użyć flagi `-d` (detached), aby uruchomić w tle:
    ```bash
    docker run -d -p 6333:6333 -p 6334:6334 qdrant/qdrant
    ```

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
