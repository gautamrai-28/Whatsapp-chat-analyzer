💬 WhatsApp Chat Analyzer

A powerful Streamlit-based web application that analyzes exported WhatsApp chat data and provides deep insights such as message statistics, activity trends, sentiment analysis, response time analysis, emoji usage, and much more.


📌 Project Overview

The WhatsApp Chat Analyzer allows users to upload their exported WhatsApp chat file and get detailed analytics including:

📊 Chat statistics

📅 Monthly & Daily timelines

📈 Activity heatmaps

😊 Sentiment analysis

⏱ Response time tracking

🧠 Message length analysis

🔥 Most active users

😂 Emoji usage insights

This project demonstrates real-world data preprocessing, NLP techniques, sentiment analysis, and data visualization using Python.



🛠 Tech Stack

- Python

- Streamlit

- Pandas

- NumPy

- Matplotlib

- Seaborn

- VADER Sentiment Analysis

- URLEXTRACT

- Emoji library



✨ Features
📊 1. Top Statistics

Total messages

Total words

Media shared count

Links shared

📅 2. Timeline Analysis

Monthly message timeline

Daily message timeline

📌 3. Activity Analysis

Most busy day

Most busy month

Weekly activity heatmap

👥 4. Most Active Users (Group Chats)

Top contributors in group chats

Percentage contribution of each user

📝 5. Most Common Words

Top 20 most frequently used words

Hinglish stopword removal support

😂 6. Emoji Analysis

Most frequently used emojis

Emoji distribution pie chart

😊 7. Sentiment Analysis

Positive / Neutral / Negative message classification

Average sentiment score calculation

⏱ 8. Response Time Analysis

Average response time (in minutes)

User-wise response comparison

✍ 9. Message Length Analysis

Average message length

User-wise message length comparison




📂 Project Structure
WhatsApp-Chat-Analyzer/
│
├── app.py                # Main Streamlit application
├── helper.py             # Analysis and statistics functions
├── preprocessor.py       # Chat data preprocessing
├── stop_hinglish.txt     # Stopwords list
├── requirements.txt      # Required dependencies
└── README.md             # Project documentation



📥 How to Export WhatsApp Chat

Open WhatsApp

Open the chat you want to analyze

Tap on:

Android → 3 dots → More → Export Chat

iPhone → Contact Info → Export Chat

Choose Without Media

Save the .txt file




▶️ How to Run Locally


1️⃣ Clone the Repository
git clone https://github.com/your-username/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv

Activate:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the App
streamlit run app.py
5️⃣ Open in Browser

Streamlit will automatically open:

http://localhost:8501


⚠️ Important Notes

Supports WhatsApp chats exported in 12-hour format (AM/PM).

Export chat without media for best results.


DEPLOYED ON STREAMLIT COMMUNITY :
https://whatsapp-chatt-analyzerr.streamlit.app/




