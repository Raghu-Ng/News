# Fetch news from NewsAPI with error handling
def fetch_news(topic):
    api_key = st.secrets["general"]["NEWS_API_KEY"]
    url = f'https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}'
    response = requests.get(url).json()
    articles = response.get("articles", [])
    news_data = []
    
    for article in articles[:5]:
        image_url = article.get("urlToImage", "")
        
        # Use a placeholder image if no valid image URL is present
        if not image_url or not image_url.startswith("http"):
            image_url = "https://via.placeholder.com/300?text=No+Image"

        news_data.append({
            "title": article["title"],
            "description": article.get("description", "No description available"),
            "image": image_url
        })
    
    return news_data

