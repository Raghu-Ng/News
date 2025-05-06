# 📰 Daily News Newsletter Bot

A beautiful Streamlit web application that allows users to:
- Select their field of interest
- View the latest news articles (with images, abstracts, and publication time)
- Subscribe to receive a daily newsletter via email

---

## ✅ What It Does

This app:
- Fetches **fresh news** using the [NewsAPI]
- Displays articles with headlines, descriptions, images, and links
- Lets users choose how many articles they want (up to the API limit)
- Sends a **daily newsletter** to users' email addresses with the latest articles in their selected category

---

## ⚙️ How It Works

### User Workflow
1. User selects a topic (e.g., Technology, Health, Sports).
2. The app fetches real-time news using NewsAPI based on their interest.
3. The user sees a clean layout of news cards with:
   - Title (linked to source)
   - Short description
   - Published time
   - Image or placeholder
4. The user can subscribe to receive these headlines daily in their email inbox.


## 📁 Project Structure
NEWS/
├── news_bot/
│ ├── app.py # Streamlit UI logic
│ ├── news_fetcher.py # NewsAPI interaction logic
│ ├── email_handler.py # Email formatting and sending
│ └── .env # (optional) Local secrets
│
├── .streamlit/
│ └── secrets.toml # Secure app credentials
│
├── requirements.txt # All dependencies
└── README.md # This file


If you like this project, give it a ⭐ on GitHub and share it with your friends!



Built by Raghava Reddy N
GitHub: Raghu-Ng

