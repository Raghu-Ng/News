import streamlit as st
from news_fetcher import fetch_news
from email_handler import send_email
import os

st.set_page_config(page_title="News Bot", layout="wide")

st.title("📩 Daily News Bot")

# Dropdown to select field of interest
interests = ["Technology", "Health", "Business", "Sports", "Entertainment"]
interest = st.selectbox("Choose your field of interest:", interests)

# Fetch and display news
if st.button("Fetch News"):
    news = fetch_news(interest)
    for item in news:
        st.image(item['image'], width=300)
        st.write(f"### {item['title']}")
        st.write(item['description'])

# Subscription
if st.checkbox("Do you want this daily?"):
    email = st.text_input("Enter your email:")
    if st.button("Subscribe"):
        news = fetch_news(interest)
        send_email(news, email)
        st.success("✅ Successfully subscribed for daily newsletter!")
