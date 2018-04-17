import re
from stanfordcorenlp import StanfordCoreNLP

text = ("We is a boy.")
text = re.sub('[^A-Za-z0-9]+', ' ', text)

nlp = StanfordCoreNLP(r'C:\Academic\NLP\stanford-corenlp-full-2018-02-27')

tags = []

pos_tags = nlp.pos_tag(text)
#print(len(pos_tags))

for i in range(len(pos_tags)):
    tags.append(pos_tags[i][1])
 
singular_PRP = ['I', 'You', 'They', 'We', 'i', 'you', 'they', 'we'] 
plural_PRP = ['He', 'She', 'It', 'he', 'she', 'it']
    
#print(tags)    

sub_verb_errors = 0

# Checking sub_verb_errors for Pronouns
for i in range(len(pos_tags)):
    if pos_tags[i][0] in singular_PRP and pos_tags[i+1][1] == 'VBZ':
        sub_verb_errors += 1
        
    elif pos_tags[i][0] in plural_PRP and pos_tags[i+1][1] == 'VBP':
        sub_verb_errors += 1        
        
    elif pos_tags[i][0] in plural_PRP and pos_tags[i+1][1] == 'VB':
        sub_verb_errors += 1

# Checking sub_verb_errors for Verb tense
sub_verb_errors += tags.count("'NN', 'VBP'")    
sub_verb_errors += tags.count("'NN', 'VB'")   
sub_verb_errors += tags.count("'NNP', 'VBP'") 
sub_verb_errors += tags.count("'NNPS', 'VBZ'")
sub_verb_errors += tags.count("'NNS', 'VBZ'")
sub_verb_errors += tags.count("'NNP', 'VB'")
sub_verb_errors += tags.count("'NN', 'WDT', 'VB'")
sub_verb_errors += tags.count("'NN', 'WDT', 'VBP'")
sub_verb_errors += tags.count("'NNS', 'WDT', 'VBZ'")
         
print(sub_verb_errors)

nlp.close()



