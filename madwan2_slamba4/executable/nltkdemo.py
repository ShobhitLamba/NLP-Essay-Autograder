#REQUIRED: Anything that needs to be downloaded, make sure you include at the beginning of your code!
import nltk

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('treebank')

#Load test.txt from the resources folder using relative path
test_file_path = 'resources/test.txt'
with open(test_file_path,'rt') as f:
	print(f.read())

#write results.txt to the output folder using relative path
results_file_path = '../output/results.txt'
fileContents = ['12345.txt;1;2;4;1;0;0;0;5;low\n','54321.txt;5;5;0;5;4;5;5;43;high']
with open(results_file_path,'w+') as f:
	for content in fileContents:
		f.write(content)


text = ("Pierre Vinken, 61 years old, will join the board as a nonexecutive director Nov. 29. " +
"Mr. Vinken is chairman of Elsevier N.V., the Dutch publishing group. " +
"Rudolph Agnew, 55 years old and former chairman of Consolidated Gold Fields PLC, " +
"was named a director of this British industrial conglomerate.")

from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
result = ""
for token in tokens:
	result += "[" + token + "] "
print(result)
print("\n=====================================================\n")

from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(text)
result = ""
for sentence in sentences:
	result += "[" + sentence + "] "
print(result)
print("\n=====================================================\n")

from nltk import pos_tag
tagged_tokens = pos_tag(tokens)
result = ""
for token in tagged_tokens:
	result += '[' + token[0] + '/' + token[1] + '] '
print(result)
print("\n=====================================================\n")

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
result = ""
for token in tokens:
	result += '[' + lemmatizer.lemmatize(token) + '] '
print(result)
print("\n=====================================================\n")

tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary = False)

for sentence in chunked_sentences:
	str_sentence =' '.join(str(sentence).split())
	str_sentence = str_sentence.replace('(','[')
	str_sentence = str_sentence.replace(')',']')
	print(str_sentence)
print("\n=====================================================\n")