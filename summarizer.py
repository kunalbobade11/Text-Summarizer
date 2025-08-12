# summarizer.py
import bs4 as bs
import urllib.request as url
import re
import nltk
import heapq
from nltk.corpus import stopwords
from string import punctuation

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

def fetch_wikipedia_article(link):
    scraped_data = url.urlopen(link)
    article = scraped_data.read()
    parsed_article = bs.BeautifulSoup(article, 'lxml')
    paragraphs = parsed_article.find_all('p')
    article_text = "".join([p.text for p in paragraphs])
    return article_text

def summarize_text(article_text, num_sentences=7):
    # Preprocessing
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    
    # Tokenization
    sentence_list = nltk.sent_tokenize(article_text)
    stop_words = stopwords.words('english')

    # Word Frequency
    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
        if word.lower() not in stop_words and word not in punctuation:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1
            
    max_freq = max(word_frequencies.values())
    word_frequencies = {word: freq/max_freq for word, freq in word_frequencies.items()}

    # Sentence Scores
    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies:
                if len(sent.split(' ')) < 30:
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

    # Top N sentences
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    return summary
