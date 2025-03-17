import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(news_list, recipient_email):
    sender_email = os.getenv("EMAIL")
    app_password = os.getenv("APP_PASSWORD")

    subject = "Your Daily Newsletter"
    body = "\n\n".join([f"{news['title']}: {news['description']}" for news in news_list])

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
