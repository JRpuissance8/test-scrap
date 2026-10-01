# test-scrap

Test de [ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai) : scraping piloté par LLM.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

`langchain-community` est bridé sous 0.4.2 : la version 0.4.2 ne fournit plus `ChatOllama` et l'import de `scrapegraphai` plante.

## Utilisation

Mettre la clé dans un fichier `.env` :

```
OPENAI_API_KEY=sk-...
```

Puis :

```bash
python example.py
```

Pour un modèle local, remplacer le bloc `llm` par `{"model": "ollama/llama3.2", "model_tokens": 8192, "format": "json"}` (Ollama doit tourner).
