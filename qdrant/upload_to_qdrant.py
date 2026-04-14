import json
import requests

QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "articles"

try:
    requests.delete(f"{QDRANT_URL}/collections/{COLLECTION_NAME}")
except:
    pass

requests.put(f"{QDRANT_URL}/collections/{COLLECTION_NAME}", json={"vectors": {"size": 384, "distance": "Cosine"}})

with open("articles_with_vectors.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

points = [{"id": i+1, "vector": a["vector"], "payload": {k: a[k] for k in ["title", "content", "author", "category", "published_at", "views", "rating"]}} for i, a in enumerate(articles)]

requests.put(f"{QDRANT_URL}/collections/{COLLECTION_NAME}/points", json={"points": points})