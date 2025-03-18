import requests
import streamlit as st
from datetime import datetime, timedelta

def fetch_news(topic):
    """Fetches the latest news articles from NewsAPI."""
    api_key = st.secrets["general"]["NEWS_API_KEY"]
    
    # Get today's date (YYYY-MM-DD)
    today = datetime.now().strftime('%Y-%m-%(d-1)')
    
    url = f'https://newsapi.org/v2/everything?q={topic}&from={today}&sortBy=publishedAt&apiKey={api_key}'
    
    response = requests.get(url).json()
    articles = response.get("articles", [])

    news_data = []
    for article in articles[:5]:
        news_data.append({
            "title": article.get("title", "No Title"),
            "description": article.get("description", "No description available"),
            "image": article.get("urlToImage", ""),
            "url": article.get("url", "#"),
            "published_at": article.get("publishedAt", "Unknown date"),
        })

    return news_data
