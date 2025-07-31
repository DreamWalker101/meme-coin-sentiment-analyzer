
# 🧠 Meme Coin Sentiment Analyzer

Analyze public sentiment of meme coins using Reddit discussions and transformer-based sentiment classification.

![UI Screenshot 1](Assets/ss1.png)
![UI Screenshot 2](Assets/ss2.png)

---

## 🚀 Features

- 🔍 **Live Reddit Scraper** using `PRAW` to fetch recent posts from selected meme coin subreddits or keyword-based searches
- 🤖 **Sentiment Analysis** powered by `cardiffnlp/twitter-roberta-base-sentiment` (pre-trained BERT model)
- 📊 **Streamlit Interface** with confidence histograms, pie charts, and labeled samples
- 📁 Clean and modular architecture, notebook version included for experimentation
- 🔁 Continuous updates for topic-specific sentiment using Telegram and n8n integrations (optional)

---

## 🛠 Installation

### 1. Clone the repo
```bash
git clone https://github.com/DreamWalker101/meme-coin-sentiment-analyzer.git
cd meme-coin-sentiment-analyzer
```

### 2. Create & activate a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # on Linux/macOS
venv\Scripts\activate   # on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 Running the App

```bash
streamlit run app.py
```

Then visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📂 File Structure

```
.
├── app.py                          # Main Streamlit application
├── meme_sentiment_experiment.ipynb  # Jupyter notebook for step-by-step exploration
├── reddit_scraper.py               # Module for Reddit data collection via PRAW
├── sentiment_analysis.py           # Text preprocessing and model prediction code
├── requirements.txt
├── Assets/
│   ├── ss1.png
│   └── ss2.png
└── README.md
```

---

## 📦 Dependencies

- `pandas`
- `streamlit`
- `transformers`
- `torch`
- `praw`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Install all dependencies via:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions, suggestions, and PRs are welcome! If you have ideas for new features (e.g., Twitter scraping, real-time updates, dashboards), feel free to fork or open an issue.

---

## 👨‍💻 Author

**Ahmed Khan** – _AI & Web Developer_  
📧 [ahmed2@on5.io](mailto:ahmed2@on5.io)  
🌐 [on5.io](https://on5.io)

---

> Built with ❤️ for data-driven decision-making in the crypto meme space.
