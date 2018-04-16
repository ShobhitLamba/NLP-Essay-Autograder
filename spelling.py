import re
import nltk
from nltk.corpus import wordnet as wn

text = ("I am happy I am a ting. Ar you as beutiphul as I think you are?")
text = re.sub('[^A-Za-z0-9]+', ' ', text)

tokens = nltk.word_tokenize(text)

#print(tokens)

count = 0

for word in tokens:
    if not wn.synsets(word):
        count += 1
        
print(count)        
