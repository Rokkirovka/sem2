import requests
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
query = "бег и спорт"
query_vector = model.encode(query).tolist()

response = requests.post("http://localhost:6333/collections/articles/points/search", json={
    "vector": query_vector,
    "limit": 3,
    "with_payload": True
})

for hit in response.json()["result"]:
    print(f"Score: {hit['score']:.3f} | {hit['payload']['title']}")

""" результат


Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]
Loading weights: 100%|██████████| 103/103 [00:00<00:00, 33968.65it/s]
[1mBertModel LOAD REPORT[0m from: sentence-transformers/all-MiniLM-L6-v2
Key                     | Status     |  | 
------------------------+------------+--+-
embeddings.position_ids | [38;5;208mUNEXPECTED[0m |  | 

Notes:
- [38;5;208mUNEXPECTED:[0m	[3mcan be ignored when loading from different task/architecture; not ok if you expect identical arch.[0m
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Score: 0.533 | Чемпионат мира по футболу
Score: 0.508 | Курс доллара упал
Score: 0.477 | Кибербезопасность 2024
"""
