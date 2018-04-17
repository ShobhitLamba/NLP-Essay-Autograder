import re
from collections import Counter
import nltk
from nltk.corpus import wordnet as wn

text = ("I believed successful people are always try new things and take risk rater than only doing what they already know it. Somehow successful people are always try to create the new things to let them to be sussessful. Therefore, mony people are usually doing things same they usually do such like jod, habies, even sport. First, people have jod are usually have the smalily then they were educaed subject in the college which they already perpared for the jod that they are going to do. However, people didn't change jod too much once they were get used to on they own jod, so that is why people make different types money and how suessful their will be. Therefore, people were being successful it is because they knew how to change their life by change their own jod. Often people try to go to school like counmmitry college again, either by learn themself from book even they were elder adults. In other way they might just by asked other people their own expenince make a ilttle change to fit in nowsday's socity. It usually makes them to be more postive to do it. Somtines people change their habies because it is just papuler for now and it is not really sure about later day or another time what is would be. Finaly, people were being successful or not is depen on what is your personal atetivies. Somehow people sucessful just for their own good, but many of other successful people I think will probably pay back for the socity, so i still believed people suessful is not just for thier own good is for every one in the would.")
text = re.sub('[^A-Za-z]+', ' ', text)

tokens = nltk.word_tokenize(text)

#print(tokens)

count = 0
wrong_words = []
for word in tokens:
    if not wn.synsets(word):
        count += 1
        wrong_words.append(word)

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

count = 0
updated_wrong_words = []

for word in wrong_words:
    if correction(word) != word:
        count += 1
        updated_wrong_words.append(word)
        
print(count)        

