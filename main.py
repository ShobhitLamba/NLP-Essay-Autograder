import nltk
from nltk.tokenize import sent_tokenize

one_essay = open('essays_dataset/essays/38209.txt', 'r').read()

def count_sentences():
    sentences = sent_tokenize(one_essay)
    print(sentences)

count_sentences()
