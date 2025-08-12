# 📝 Automatic Text Summarizer

A **Flask-based web application** that takes long text as input and returns a concise, meaningful summary using **Natural Language Processing (NLP)** techniques such as **tokenization**, **stop word removal**, **frequency-based scoring**, and **sentence extraction**.  

This project is designed for **ease of use** with a **modern, responsive UI** using HTML, CSS, and JavaScript.

---

## 🚀 Features

- 📄 **Summarize Any Text** — Paste long content and get a short, crisp summary.
- 🌐 **Web-based Interface** — Works in your browser (desktop & mobile-friendly).
- ⚡ **Fast Processing** — Uses frequency-based summarization for quick results.
- 📦 **Modular Codebase** — Backend and frontend are separated for maintainability.
- 🎨 **Clean & Modern UI** — Custom styling and responsive design.
- 🔄 **Reset Option** — One-click clear button to start fresh.
- 🛠 **Easily Extensible** — Add Wikipedia URL summarization or NLP model upgrades.

---

## 📂 Project Structure

```
text_summarizer_project/
│
├── app.py                 # Flask backend application
├── summarizer.py          # Core summarization logic
├── requirements.txt       # Python dependencies
│
├── templates/             # HTML templates (served by Flask)
│   └── index.html         # Main UI page
│
├── static/                # Static assets
│   ├── style.css          # Styling for the UI
│   └── script.js          # JavaScript for interactivity
│
└── README.md              # Project documentation
```

---

## 🛠 Installation & Setup

### 1️⃣ Clone the repository
```
git clone https://github.com/kunalbobade11/text_summarizer_project.git
cd Text Summarizer
```

### 2️⃣ Install dependencies
Make sure you have **Python 3.7+** installed.

```
pip install -r requirements.txt
```

### 3️⃣ NLTK Data Setup
The first time you run the app, it will automatically download required **NLTK corpora** (`punkt`, `stopwords`).  
You can also download them manually:

```
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### 4️⃣ Run the application
```
python app.py
```

### 5️⃣ Open in Browser
Go to:
```
http://127.0.0.1:5000
```

---

## 💻 Usage

1. Open the app in your browser.  
2. **Paste or type text** you want to summarize in the input box.  
3. Click **Summarize** to process the text.  
4. The summarized version will appear instantly in the output box.  
5. Use **Clear** to reset the fields.

---

## 🧠 How it Works

1. **Input Text** — User enters/pastes text.
2. **Text Cleaning** — Removes special characters, references, and extra spaces.
3. **Tokenization** — Splits text into words & sentences.
4. **Stop Word Removal** — Removes non-informative words.
5. **Word Frequency Calculation** — Counts word importance.
6. **Sentence Scoring** — Assigns scores to sentences based on key words.
7. **Sentence Selection** — Picks top-ranked sentences to form the summary.
8. **Output** — Displays the summary to the user.

---

## 📦 Dependencies

- **Flask** — Web framework.
- **BeautifulSoup4** — HTML parsing (if using Wikipedia fetching).
- **lxml** — Additional parsing support.
- **nltk** — Natural Language Toolkit for tokenization & stop words.

Install them via:
```
pip install flask beautifulsoup4 lxml nltk
```

---

## 🔮 Possible Extensions

- 📰 **Wikipedia Article Summarization** — Paste a Wikipedia URL and summarize automatically.
- 🧠 **Deep Learning Models** — Use transformer-based summarizers like **BERT** or **T5**.
- 🌍 **Multi-language Support** — Add support for non-English languages.
- 📊 **Summarization Length Control** — Let users choose summary length.

---

## 📷 Screenshot (Example)

```
+------------------------------------------------------+
|        Automatic Text Summarizer                     |
|-------------------------------------------------------|
| [ Paste your text here...                         ]  |
| [ Summarize ]   [ Clear ]                            |
|-------------------------------------------------------|
| Summary:                                              |
| "This is your generated summary."                     |
+------------------------------------------------------+
```

---

## 📜 License

This project is **open-source** under the **MIT License** — you can use and modify it for personal or commercial purposes.

---
