import streamlit as st

st.write("✅ App has started")

# rest of your code...

import streamlit as st
import praw
import pandas as pd
import re
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------
# HARD-CODED REDDIT KEYS
# ---------------------
reddit = praw.Reddit(
    client_id="hYZF0K7MCM66chv4--t8tg",
    client_secret="MnvHuP7yhAoAjoRuS1TsYDNymd5GEg",
    user_agent="meme-coin-sentiment-analyzer"
)

# ---------------------
# LOAD BERT MODEL
# ---------------------
@st.cache_resource
def load_model():
    model_name = "cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# ---------------------
# SENTIMENT FUNCTION
# ---------------------
def predict_sentiment(text, tokenizer, model):
    encoded_input = tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
    with torch.no_grad():
        output = model(**encoded_input)
    scores = softmax(output.logits.numpy()[0])
    sentiment = ['negative', 'neutral', 'positive'][scores.argmax()]
    confidence = float(scores.max())
    return sentiment, confidence

# ---------------------
# CLEAN TEXT
# ---------------------
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r"[^A-Za-z0-9\s]+", '', text)
    text = text.strip()
    return text

# ---------------------
# MAIN STREAMLIT APP
# ---------------------
st.set_page_config(page_title="Meme Coin Sentiment Analyzer", layout="centered")
st.title("📈 Meme Coin Sentiment Analyzer")
st.markdown("Analyze Reddit sentiment in any crypto-related subreddit using BERT!")

# FORM INPUT
with st.form("input_form"):
    subreddit_name = st.text_input("Enter subreddit name (without r/):", value="dogecoin")
    post_limit = st.number_input("Number of posts to analyze", min_value=10, max_value=300, step=10, value=100)
    submitted = st.form_submit_button("🔍 Analyze Sentiment")

if submitted:
    with st.spinner("Fetching and analyzing posts..."):
        posts = []
        try:
            for post in reddit.subreddit(subreddit_name).hot(limit=int(post_limit)):
                title = post.title or ""
                body = post.selftext or ""
                full_text = title + " " + body
                clean = clean_text(full_text)
                if clean:
                    sentiment, confidence = predict_sentiment(clean, tokenizer, model)
                    posts.append({
                        "title": title,
                        "clean_text": clean,
                        "sentiment": sentiment,
                        "confidence": confidence
                    })
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.stop()

    if not posts:
        st.warning("No valid posts found.")
        st.stop()

    df = pd.DataFrame(posts)

    # Show results
    st.subheader("📊 Sentiment Distribution")
    sentiment_counts = df["sentiment"].value_counts().reindex(['positive', 'neutral', 'negative'], fill_value=0)
    st.bar_chart(sentiment_counts)

    # Optional: confidence histogram
    st.subheader("🔎 Confidence Levels")
    st.pyplot(sns.histplot(data=df, x="confidence", bins=10, kde=True).figure)

    # Show table
    st.subheader("📋 Detailed Results")
    st.dataframe(df[["title", "sentiment", "confidence"]])

