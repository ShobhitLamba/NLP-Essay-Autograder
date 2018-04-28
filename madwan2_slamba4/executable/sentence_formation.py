from nltk.tokenize import sent_tokenize

def check_sentence_formation(dot_processed_sentences, nlp):
    print("insizkdfbidsfj ")
    for sentence in dot_processed_sentences:
        pos_tags = nlp.pos_tag(sentence)
        parse_tree = nlp.parse(sentence)
        print(pos_tags)
