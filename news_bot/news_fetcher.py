import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_news(topic):
    api_key = os.getenv("NEWS_API_KEY")
    url = f'https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}'
    response = requests.get(url).json()
    articles = response.get("articles", [])
    news_data = []

    for article in articles[:5]:  
        news_data.append({
            "title": article["title"],
            "description": article.get("description", "No description available"),
            "image": article.get("urlToImage", "")
        })

    return news_data
