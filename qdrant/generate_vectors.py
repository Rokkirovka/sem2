from sentence_transformers import SentenceTransformer
import json

model = SentenceTransformer('all-MiniLM-L6-v2')


articles = [
    {
        "title": "Новый iPhone 15 обзор",
        "content": "Apple представила iPhone 15 с новым процессором и камерой 48MP",
        "author": "Иван Иванов",
        "category": "tech",
        "published_at": "2024-03-15",
        "views": 15000,
        "rating": 4.8
    },
    {
        "title": "Марафон в Москве 2024",
        "content": "Тысячи бегунов приняли участие в ежегодном марафоне по улицам Москвы",
        "author": "Петр Петров",
        "category": "sport",
        "published_at": "2024-05-20",
        "views": 8000,
        "rating": 4.5
    },
    {
        "title": "Выборы президента 2024",
        "content": "В России прошли выборы президента, явка составила 70%",
        "author": "Анна Сидорова",
        "category": "news",
        "published_at": "2024-03-18",
        "views": 50000,
        "rating": 4.2
    },
    {
        "title": "ChatGPT 5 анонсирован",
        "content": "OpenAI представила новую версию языковой модели с поддержкой видео",
        "author": "Дмитрий Козлов",
        "category": "tech",
        "published_at": "2024-04-01",
        "views": 25000,
        "rating": 4.9
    },
    {
        "title": "Чемпионат мира по футболу",
        "content": "Сборная Бразилии выиграла чемпионат мира, победив Аргентину в финале",
        "author": "Карлос Сантос",
        "category": "sport",
        "published_at": "2024-07-10",
        "views": 35000,
        "rating": 4.7
    },
    {
        "title": "Кибербезопасность 2024",
        "content": "Новые угрозы и методы защиты данных в корпоративном секторе",
        "author": "Елена Смирнова",
        "category": "tech",
        "published_at": "2024-02-10",
        "views": 6000,
        "rating": 4.0
    },
    {
        "title": "Летние Олимпийские игры",
        "content": "Париж готовится принять Олимпиаду 2024, построены новые стадионы",
        "author": "Жан Дюпон",
        "category": "sport",
        "published_at": "2024-06-01",
        "views": 28000,
        "rating": 4.6
    },
    {
        "title": "Курс доллара упал",
        "content": "Центробанк снизил ключевую ставку, курс доллара упал до 80 рублей",
        "author": "Сергей Морозов",
        "category": "news",
        "published_at": "2024-04-20",
        "views": 45000,
        "rating": 3.9
    }
]

for article in articles:
    text = article["title"] + ". " + article["content"]
    vector = model.encode(text).tolist()
    article["vector"] = vector


with open("articles_with_vectors.json", "w", encoding="utf-8") as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)