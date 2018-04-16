import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import os
import re

def count_sentences():
    temp_flag = False

    ''' Get the list of sentences'''
    sentences = sent_tokenize(one_essay)
    tagged_sentences = []
    processed_sentences = []

    ''' Convert all the sentences which have new line char into multiple sentences '''
    for sentence_index, sentence in enumerate(sentences):
        temp_sentence = sentence.strip().replace('\n\n', '\n').replace('\n\n\n', '\n')

        for split_sentence in temp_sentence.split('\n'):
            processed_sentences.append(split_sentence.strip())

    for sentence_index, sentence in enumerate(processed_sentences):
        temp_sentence = sentence.strip('.')
        if temp_sentence.find('.') != -1:
            # print(temp_sentence)
            # print('###############################################')
            pass
            # temp_flag = True

        ''' Get the pos tag in each sentence after tokenizing it'''
        tagged_sentences.append(pos_tag(word_tokenize(sentence.strip())))

        ''' To process the sentences more by POS tags and capitalization '''
        for tagged_token_index, tagged_token in enumerate(tagged_sentences[sentence_index]):
            if tagged_token_index != 0: # Ignore 1st word
                '''
                    The previous tag should be alpha and not characters (: , ")
                    and it shouldn't be CC (coordinate conjunction) or IN (subordinate conjunction)
                    otherwise it will be a valid sentence.
                '''
                if tagged_sentences[sentence_index][tagged_token_index - 1][1].isalpha() and tagged_sentences[sentence_index][tagged_token_index - 1][1] != 'CC' and tagged_sentences[sentence_index][tagged_token_index - 1][1] != 'IN':
                    '''
                        Capitalization logic. If the word is capitalized and not an I or proper noun or noun then new sentence
                    '''
                    if tagged_token[0][0].isupper():
                    # if tagged_token[0][0].isupper() and tagged_token[0] != 'I' and tagged_token[1] != 'NNP' and tagged_token[1] != 'NN' and tagged_token[1] != 'NNS':
                        # temp_flag = True
                        print(tagged_sentences[sentence_index][tagged_token_index - 1][1])
                        print(tagged_sentences[sentence_index])
                        print(sentence)
                        print(tagged_token)

    if temp_flag and filename_index > 0:
        print('------------------------------------------------------------------------------------')
        print(filename)
        print(sentences)
        print(one_essay)
        print('************************************************************************************************************************************************')


''' Get the list of filenames to iterate over one by one'''
filenames = os.listdir('essays_dataset/essays/')
# filename = 'essays_dataset/essays/' + '38209.txt'
print(len(filenames))
for filename_index, filename in enumerate(filenames):
    filepath = 'essays_dataset/essays/' + filename

    ''' Read file '''
    file = open(filepath, 'r')
    one_essay = file.read()

    count_sentences()

    print("******************ENd of 1 essay *********************************************")
    file.close()
    if filename_index == 30:
        break
        pass
