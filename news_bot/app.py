import streamlit as st
from news_fetcher import fetch_news
from email_handler import send_email

st.title("Daily News Newsletter")

# Streamlit Cache Buster
st.cache_data.clear()

interests = ["Technology", "Health", "Business", "Sports", "Entertainment"]
interest = st.selectbox("Choose your field of interest:", interests)

if st.button("Fetch News"):
    news = fetch_news(interest)
    
    if news:
        for item in news:
            st.image(item["image"], width=300)
            st.write(f"### [{item['title']}]({item['url']})")
            st.write(f"🕒 Published: {item['published_at']}")
            st.write(item["description"])
    else:
        st.error("No fresh news found!")

# Email Subscription
if st.checkbox("Do you want this daily?"):
    email = st.text_input("Enter your email:")
    if st.button("Subscribe"):
        if email:
            news = fetch_news(interest)
            send_email(news, email)
            st.success("Newsletter subscription successful!")
        else:
            st.error("Please enter a valid email!")
