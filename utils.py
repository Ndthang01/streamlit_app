import re
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

def text_preprocessing(text,stopword):
    # lowercase
    text = text.lower()

    # Remove URL
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Remove user @ references and ‘#’ from text
    text = re.sub(r'\@\w+|\#','', text)

    # Remove punctuations
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)


    # Tokenize to remove stopwords
    text_tokens = word_tokenize(text)

    # Remove stopwords
    # Remove stopwords
    cleaned_text = ' '
    tokens_without_sw = [cleaned_text.join(word) for word in text_tokens if word not in stopword]

    return tokens_without_sw
