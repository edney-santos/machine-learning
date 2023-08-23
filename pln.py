import pandas as pd
import string
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import random
import seaborn as sns
import numpy as np
import re

dataframe = pd.read_csv('./data/IMDB_Dataset.csv', lineterminator="\n")

punctuation = string.punctuation
stop_words = STOP_WORDS

nlp = spacy.load('en_core_web_sm')

def text_preprocessing(text: string):
    clean_text = re.sub(r'<.*?>', '', text).lower()
    document = nlp(clean_text)
    words = []

    for token in document:
        words.append(token.lemma_)

    words = [word for word in words if word not in stop_words and word not in punctuation]
    words = ' '.join([str(element) for element in words if not element.isdigit()])

    return words

dataframe['review'] = dataframe['review'].apply(text_preprocessing)

print(dataframe.head())