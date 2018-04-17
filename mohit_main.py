import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import os
import re

from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://localhost', port=9000)
# nlp = StanfordCoreNLP(r'../stanford-corenlp-full-2017-06-09')
# sentence = 'She was waiting in the room and he came in.'
# print(nlp.parse(sentence))


def count_sentences():
    length_of_essay = 0
    ''' Get the list of sentences'''
    sentences = sent_tokenize(one_essay)
    tagged_sentences = []
    processed_sentences = []

    ''' Convert all the sentences which have new line char into multiple sentences '''
    for sentence_index, sentence in enumerate(sentences):
        temp_sentence = sentence.strip().replace('\n\n', '\n').replace('\n\n\n', '\n')

        for split_sentence in temp_sentence.split('\n'):
            processed_sentences.append(split_sentence.strip())

    ''' if a dot has a alpha after it, consider it as a new line '''
    dot_processed_sentences = []
    for sentence_index, sentence in enumerate(processed_sentences):
        temp_sentence = sentence
        temp_sentences_list = []
        dot_index = 0
        while dot_index < len(temp_sentence) - 1:
            dot_index = temp_sentence.find('.', dot_index)
            if dot_index == -1:
                temp_sentences_list.append(temp_sentence)
                break
            ''' if the next char after . is alpha and there should be atleast 2 characters after the . '''
            if dot_index < len(temp_sentence) - 3:
                if temp_sentence[dot_index + 1].isalpha() and temp_sentence[dot_index - 1] != '.':
                    temp_sentences_list.append(temp_sentence[:dot_index+1])
                    temp_sentence = temp_sentence[dot_index+1:]
                    dot_index = 0
            else:
                temp_sentences_list.append(temp_sentence)
                break
            dot_index = dot_index + 1

        for dot_sentence in temp_sentences_list:
            dot_processed_sentences.append(dot_sentence)


    if len(dot_processed_sentences) != len(processed_sentences):
        # print(len(dot_processed_sentences), len(processed_sentences))
        pass

    # return len(dot_processed_sentences)
    temp_flag = False

    length_of_essay = len(dot_processed_sentences)
    ''' Processing based on POS tags and finite verb '''
    for sentence_index, sentence in enumerate(dot_processed_sentences):
        ''' Get the pos tag in each sentence after tokenizing it'''
        # parse_tree = nlp.parse(sentence.strip())
        parse_tree = nlp.parse(sentence.strip()).split()
        if '(SBAR' in parse_tree:
            if parse_tree[parse_tree.index('(SBAR') + 1] == '(S':
                length_of_essay += 1


        # tagged_sentence = (nlp.pos_tag(sentence.strip()))
        # parsed_sentence = nlp.dependency_parse(sentence.strip())
        #
        # finite_verb_count = 0
        # for parsed_token_index, parsed_token in enumerate(parsed_sentence):
        #     if parsed_token[0] == 'nsubj':
        #         if finite_verb_count > 0:
        #             previous_token_index = parsed_token[2] - 1
        #             if tagged_sentence[previous_token_index][1].isalpha() and tagged_sentence[previous_token_index][1] != 'CC' and tagged_sentence[previous_token_index][1] != 'IN':
        #                 finite_verb_count += 1
        #                 print(parsed_token)
        #                 print(tagged_sentence[previous_token_index:])
        #         else:
        #             finite_verb_count += 1
        #
        # if finite_verb_count > 1:
        #     print(parse_tree)
        #     print(sentence)
        #     print(tagged_sentence)
        #     print(parsed_sentence)


    return length_of_essay
        # ''' To process the sentences more by POS tags and capitalization '''
        # for tagged_token_index, tagged_token in enumerate(tagged_sentence):
        #     if tagged_token_index != 0: # Ignore 1st word
        #         '''
        #             The previous tag should be alpha and not characters (: , ")
        #             and it shouldn't be CC (coordinate conjunction) or IN (subordinate conjunction)
        #             otherwise it will be a valid sentence.
        #         '''
        #         if tagged_sentence[tagged_token_index - 1][1].isalpha() and tagged_sentence[tagged_token_index - 1][1] != 'CC' and tagged_sentence[tagged_token_index - 1][1] != 'IN':
        #             '''
        #                 Capitalization logic. If the word is capitalized and not an I or proper noun or noun then new sentence
        #                 (Doesn't work. Only 2 percent accuracy. will have more negative effect than positive)
        #
        #             # if tagged_token[0][0].isupper() and tagged_token[0] != 'I' and tagged_token[1] != 'NNP'
        #             if tagged_token[0][0].isupper() and tagged_token[0] != 'I' and tagged_token[1] != 'NNP' and tagged_token[1] != 'NN' and tagged_token[1] != 'NNS':
        #                 # temp_flag = True
        #                 print(filename)
        #                 print(tagged_sentences[sentence_index][tagged_token_index - 1][1])
        #                 print(tagged_sentences[sentence_index])
        #                 print(sentence)
        #                 print(tagged_token)
        #
        #             '''
        #             pass

    if temp_flag and filename_index > 0:
        print('------------------------------------------------------------------------------------')
        print(filename)
        print(sentences)
        print(one_essay)
        print('************************************************************************************************************************************************')



csv_file = open('essays_dataset/index.csv', 'r')
line_index = 0

total_essay = [0, 0] # [low high]
avg_essay_length = [0, 0] # [low high]

for line in csv_file:
    if line_index != 0:
        line_list = line.split(';')
        filepath = 'essays_dataset/essays/' + line_list[0]

        ''' Read file '''
        essay_file = open(filepath, 'r')
        one_essay = essay_file.read()

        essay_len = count_sentences()
        if line_list[2].strip().lower() == 'low':
            # print('low')
            total_essay[0] += 1
            avg_essay_length[0] += essay_len
        else:
            # print('High')
            total_essay[1] += 1
            avg_essay_length[1] += essay_len
        print(essay_len)
        print("******************ENd of", line_index, "essay *********************************************")

        essay_file.close()
        if line_index == 1:
            # break
            pass
    line_index += 1

csv_file.close()
print(total_essay, avg_essay_length)
avg_essay_length[0] = avg_essay_length[0]/total_essay[0]
avg_essay_length[1] = avg_essay_length[1]/total_essay[1]
print(total_essay, avg_essay_length)
nlp.close()
