import requests
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
query = "технологии"
query_vector = model.encode(query).tolist()

response = requests.post("http://localhost:6333/collections/articles/points/search", json={
    "vector": query_vector,
    "limit": 10,
    "with_payload": True,
    "filter": {
        "must": [
            {"key": "category", "match": {"value": "tech"}},
            {"key": "rating", "range": {"gte": 4.0}}
        ]
    }
})

for hit in response.json()["result"]:
    print(f"Score: {hit['score']:.3f} | {hit['payload']['title']} | rating: {hit['payload']['rating']}")


""" результат

Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 10538.71it/s]
[1mBertModel LOAD REPORT[0m from: sentence-transformers/all-MiniLM-L6-v2
Key                     | Status     |  | 
------------------------+------------+--+-
embeddings.position_ids | [38;5;208mUNEXPECTED[0m |  | 

Notes:
- [38;5;208mUNEXPECTED:[0m	[3mcan be ignored when loading from different task/architecture; not ok if you expect identical arch.[0m
Score: 0.384 | ChatGPT 5 анонсирован | rating: 4.9
Score: 0.339 | Новый iPhone 15 обзор | rating: 4.8
Score: 0.330 | Кибербезопасность 2024 | rating: 4.0
"""
