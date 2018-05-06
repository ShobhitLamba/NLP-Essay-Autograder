import json
from nltk.corpus import wordnet as wn
# import genderPredictor as gp

third_person_s = [
'he',
'she',
'him',
'her',
'his'
# 'it',
# 'its',
]
third_person_p = [
'they',
'them',
'their'
]

props={'annotators': 'ner, dcoref','pipelineLanguage':'en','outputFormat':'json'}
nlp = None;

def check_pronoun_coherence(dot_processed_sentences, nlp):
    globals()['nlp'] = nlp
    num_mistakes = 0
    pos_tagged_sentences = []
    # temp_var = json.loads(nlp.annotate(' '.join(dot_processed_sentences), properties=props))
    # temp_var = json.loads(nlp.annotate(' '.join(dot_processed_sentences), properties=props))

    # print(list(temp_var['corefs'].keys()))
    # print(list(temp_var.keys()))
    # print(list(temp_var['sentences'][0].keys()))
    # for something in temp_var['sentences']:
    #     for something2 in something['entitymentions']:
    #         print(something2['text'], something2['ner'])
            # print(something2)
    # print(temp_var['sentences'][0]['entitymentions'])
    # print(temp_var['corefs']['1'])
    # print(json.dumps(temp_var, indent=4, sort_keys=True))

    ''' Get the sentences pos tagged '''
    for sent_index, sentence in enumerate(dot_processed_sentences):
        pos_tags = nlp.pos_tag(sentence)
        # n_e_r = nlp.ner(sentence)

        # for something in n_e_r:
        #     if something[1] != 'O':
        #         print(something)

        pos_tagged_sentences.append(pos_tags)

    for sent_index, sentence in enumerate(pos_tagged_sentences):
        for tag_index, tag in enumerate(sentence):
            ''' if a pronoun is found (PRP and PRP$) '''
            if 'PRP' in tag[1]:
                ''' if the pronoun is third person singular '''
                if tag[0].strip().lower() in third_person_s:
                    ''' if pronoun is in the first sentence then pass current sentence only. '''
                    if sent_index == 0:
                        sentences_to_check = []
                        sentences_to_check.append(sentence) # current sentence
                        error_found = check_s_pronoun(sentences_to_check, tag, tag_index)
                        # break
                    elif sent_index == 1:
                        ''' pass 2 sentences, current and current - 1. Current - 2 cannot be pass '''
#                        print('\n******************** second sentence*********************')
                        sentences_to_check = []
                        sentences_to_check.append(sentence) # current sentence
                        sentences_to_check.append(pos_tagged_sentences[sent_index-1]) # current sentence
                        error_found = check_s_pronoun(sentences_to_check, tag, tag_index)
                    else:
                        ''' pass 3 sentences, current, current - 1, current -2 '''
#                        print('\n******************** other sentence*********************')
                        sentences_to_check = []
                        sentences_to_check.append(sentence) # current sentence
                        sentences_to_check.append(pos_tagged_sentences[sent_index-1]) # previous sentence
                        sentences_to_check.append(pos_tagged_sentences[sent_index-2])
                        error_found = check_s_pronoun(sentences_to_check, tag, tag_index)
                    if error_found:
                        num_mistakes += 1
                        # break
                ''' if the pronoun is third person plural '''
                if tag[0].strip().lower() in third_person_p:
                    ''' if pronoun is in the first sentence '''
                    if sent_index == 0:
                        sentences_to_check = []
                        sentences_to_check.append(sentence) # current sentence
                        error_found = check_p_pronoun(sentences_to_check, tag, tag_index)
                        # break
                    elif sent_index == 1:
                        ''' pass 2 sentences, current, current - 1. Current - 2 cannot be pass '''
#                        print('\n******************** second sentence*********************')
                        sentences_to_check = []
                        sentences_to_check.append(sentence) # current sentence
                        sentences_to_check.append(pos_tagged_sentences[sent_index-1]) # current sentence
                        error_found = check_p_pronoun(sentences_to_check, tag, tag_index)
                    else:
                        ''' pass 3 sentences, current, current - 1, current -2 '''
#                        print('\n******************** other sentence*********************')
                        sentences_to_check = []
                        sentences_to_check.append(sentence) # current sentence
                        sentences_to_check.append(pos_tagged_sentences[sent_index-1]) # previous sentence
                        sentences_to_check.append(pos_tagged_sentences[sent_index-2])
                        error_found = check_p_pronoun(sentences_to_check, tag, tag_index)
                    if error_found:
                        num_mistakes += 1
                        # break

    return num_mistakes

def check_s_pronoun(sentences_to_check, p_tag, p_tag_index):
    for sent_index, sentence in enumerate(sentences_to_check):
        ''' if first sentence, then check previous tags'''
        if sent_index == 0:
            sentence = sentence[:p_tag_index]
        ''' Check the word in wordnet list. if its a noun.person or noun.body then return false '''
        for tag_index, tag in enumerate(sentence):
            if 'NN' == tag[1]:
                syn_set = wn.synsets(tag[0], pos=wn.NOUN)
                for syn in syn_set:
                    lex_name = syn.lexname()
                    if (lex_name == 'noun.person' or lex_name == 'noun.body'):
                        # print(p_tag, tag, lex_name, syn)
                        return False # refernce is found hence no error
            if 'NNP' == tag[1]:
                # TOIMPLEMENT - if the NNP is a person, then return false
                person_or_not = nlp.ner(tag[0])
                if person_or_not[0][1] == u'PERSON':
                    return False

#    print(sentences_to_check, p_tag)
    return True # didn't find reference - Error found

def check_p_pronoun(sentences_to_check, p_tag, p_tag_index):
    for sent_index, sentence in enumerate(sentences_to_check):
        ''' if first sentence, then check previous tags'''
        if sent_index == 0:
            sentence = sentence[:p_tag_index]
        ''' Check the word in wordnet list. if its a noun.group then return false '''
        for tag_index, tag in enumerate(sentence):
            if 'NNS' == tag[1]:
                syn_set = wn.synsets(tag[0], pos=wn.NOUN)
                for syn in syn_set:
                    lex_name = syn.lexname()
                    # if tag[0].lower() == 'cigarettes' or tag[0].lower() == 'advertisements':
                    #     print(p_tag, lex_name, tag)

                    if (lex_name == 'noun.person' or lex_name == 'noun.body' or lex_name == 'noun.group'):
                        # print(p_tag, tag, lex_name, syn)
                        return False
            if 'NNPS' == tag[1]:
                # TOIMPLEMENT - if the NNPS is a group, then return False
                group_or_not = nlp.ner(tag[0])
                if group_or_not[0][1] == u'GROUP':
                    return False
                
#    print(sentences_to_check, p_tag)
    return True
