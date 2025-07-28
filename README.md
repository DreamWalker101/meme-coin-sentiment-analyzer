
# 🚀 Meme Coin Sentiment Analyzer

A real-time Reddit sentiment analysis app focused on meme coins, powered by BERT and built with Streamlit. This project fetches live Reddit posts from crypto-related subreddits and analyzes their sentiment using a transformer-based model trained on tweets.

---

## 📌 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Details](#-model-details)
- [Project Structure](#-project-structure)
- [License](#-license)

---

## 🎯 Features

✅ Live Reddit scraping via `praw`  
✅ Sentiment analysis using [cardiffnlp/twitter-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)  
✅ Interactive Streamlit dashboard  
✅ Clean visualizations using Seaborn & Matplotlib  
✅ Confidence scoring for each prediction  
✅ No database or backend required – just run and analyze  

---

## 🌐 Demo

> 🔗 Coming soon on [Streamlit Cloud](https://streamlit.io/cloud)

![Screenshot](https://user-images.githubusercontent.com/0000000/your-image.png)  
*A sample visualization of sentiment distribution on r/dogecoin*

---

## 💻 Installation

Clone this repository:

```bash
git clone https://github.com/DreamWalker101/meme-coin-sentiment-analyzer.git
cd meme-coin-sentiment-analyzer
```

Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

You will be redirected to your browser at `http://localhost:8501`, where you can:

- Enter a subreddit (e.g., `dogecoin`)
- Choose the number of posts to analyze
- Click **Analyze Sentiment** to see:
  - Sentiment breakdown (Positive/Neutral/Negative)
  - Confidence histogram
  - Full table of predictions

---

## 🤖 Model Details

We use the HuggingFace model:  
**`cardiffnlp/twitter-roberta-base-sentiment`**

- Pretrained on ~124M tweets
- Fine-tuned for sentiment classification (positive, neutral, negative)
- High performance on short, informal text like Reddit posts

This makes it ideal for meme coin-related content, which often includes slang, emojis, and sarcasm.

---

## 🗂 Project Structure

```
meme-coin-sentiment-analyzer/
├── app.py                      # Main Streamlit app
├── meme_sentiment_experiment.ipynb  # Research & prototyping
├── requirements.txt           # Python dependencies
├── .gitignore                 # Ignored files/folders (e.g., venv/)
└── README.md                  # You're here
```

---

## 📜 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute it for personal or commercial purposes.

---

## 🤝 Contributing

If you’d like to:

- Add support for more subreddits
- Improve the model or visualizations
- Deploy the app online

Please feel free to fork and open a pull request or issue 🙌

---

## 🧠 Credits

- [Ahmed Khan](https://github.com/DreamWalker101) – Developer & Architect  
- [Cardiff NLP](https://huggingface.co/cardiffnlp) – Sentiment model  
- [Streamlit](https://streamlit.io) – Frontend framework  
- [PRAW](https://praw.readthedocs.io/) – Reddit API wrapper  
