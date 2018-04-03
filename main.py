import nltk
from nltk.tokenize import sent_tokenize

one_essay = open('essays_dataset/essays/38209.txt', 'r').read()
sentences = sent_tokenize(one_essay)
# print(sentences)
result = ""
for sentence in sentences:
	result += "[" + sentence + "] "
print(result)
