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

props={'annotators': 'ner','pipelineLanguage':'en','outputFormat':'json'}
nlp = None;

def check_pronoun_coherence(dot_processed_sentences, nlp):
    globals()['nlp'] = nlp
    num_mistakes = 0
    pos_tagged_sentences = []
    ''' Get the sentences pos tagged '''
    for sent_index, sentence in enumerate(dot_processed_sentences):
        pos_tags = nlp.pos_tag(sentence)
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
                        ''' pass 2 sentences, current, current - 1. Current - 2 cannot be pass '''
                        print('\n******************** second sentence*********************')
                        sentences_to_check = []
                        sentences_to_check.append(sentence) # current sentence
                        sentences_to_check.append(pos_tagged_sentences[tag_index-1]) # current sentence
                        error_found = check_s_pronoun(sentences_to_check, tag, tag_index)
                    else:
                        ''' pass 3 sentences, current, current - 1, current -2 '''
                        print('\n******************** other sentence*********************')
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
                        print('\n******************** second sentence*********************')
                        sentences_to_check = []
                        sentences_to_check.append(sentence) # current sentence
                        sentences_to_check.append(pos_tagged_sentences[tag_index-1]) # current sentence
                        error_found = check_p_pronoun(sentences_to_check, tag, tag_index)
                    else:
                        ''' pass 3 sentences, current, current - 1, current -2 '''
                        print('\n******************** other sentence*********************')
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
        for tag_index, tag in enumerate(sentence):
            if 'NN' == tag[1] or 'NNP' == tag[1]:
                print(tag)
                # TOIMPLEMENT - if the noun or NNP is a person, then check the gender.
                # if found then return false

    print(sentences_to_check, p_tag)
    return True

def check_p_pronoun(sentences_to_check, p_tag, p_tag_index):
    for sent_index, sentence in enumerate(sentences_to_check):
        ''' if first sentence, then check previous tags'''
        if sent_index == 0:
            sentence = sentence[:p_tag_index]
        for tag_index, tag in enumerate(sentence):
            if 'NNS' == tag[1] or 'NNPS' == tag[1]:
                print(tag)
                # TOIMPLEMENT - if the noun or NNP is a person, then check the gender.
                # if found then return false

    print(sentences_to_check, p_tag)
    return True
