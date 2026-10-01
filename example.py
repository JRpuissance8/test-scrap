import json
import os

from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph

load_dotenv()

graph_config = {
    "llm": {
        "api_key": os.environ["OPENAI_API_KEY"],
        "model": "openai/gpt-4o-mini",
    },
    "verbose": True,
    "headless": True,
}

smart_scraper_graph = SmartScraperGraph(
    prompt="Extrais la description de l'entreprise, les fondateurs et les liens réseaux sociaux",
    source="https://scrapegraphai.com/",
    config=graph_config,
)

result = smart_scraper_graph.run()
print(json.dumps(result, indent=4, ensure_ascii=False))
