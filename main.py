import nltk
from nltk.tokenize import sent_tokenize
import os

filenames = os.listdir('essays_dataset/essays/')
filename = 'essays_dataset/essays/' + filenames[0]
one_essay = open(filename, 'r').read()

def count_sentences():
    sentences = sent_tokenize(one_essay)
    for sentence in sentences:
        print(sentence)

count_sentences()
