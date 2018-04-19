from nltk import pos_tag
from nltk.tokenize import word_tokenize

verbs = [
	"MD",
	"VB",
	"VBZ",
	"VBD",
	"VBG",
	"VBN",
	"VBP",
    "TO"
]

verbs_with_adverb = [
	"MD",
	"VB",
	"VBZ",
	"VBD",
	"VBG",
	"VBN",
	"VBP",
    "RB"
]

fourgram_rules = [

"VBZ, RB, VBN, VBN",
"VBZ, RB, VBN, VBG",
"MD, RB, VB, VBG",
"MD, RB, VB, VBN"

]

trigram_rules = [

"VBZ, VBN, VBN",
"VBZ, VBN, VBG",
"MD, VB, VBG",
"MD, VB, VBN",

"VBZ, RB, VBG",
"VBZ, RB, VBN",
"VBZ, RB, VB",

"VBP, RB, VBG",
"VBP, RB, VBN",
"VBP, RB, VB",

"VBD, RB, VBG",
"VBD, RB, VBN",
"VBD, RB, VB",

"MD, RB, VB",

"TO, RB, VB"
]

bigram_rules = [

"VBZ, VBG",
"VBZ, VBN",
"VBZ, VB",

"VBP, VBG",
"VBP, VBN",
"VBP, VB",

"VBD, VBG",
"VBD, VBN",
"VBD, VB",

"MD, VB",

"TO, VB",

"VBP, RB", #- I am finally fine.
"VBZ, RB", #- He is finally fine
"VBD, RB", #- He sang finally.

]

unigram_rules = [

"VBP", #- I am fine.
"VBZ", #- He is fine
"VBD", #- He sang.
"VBG", # - Having some understanding is good
"TO" # from one to another

]


def verb_tense(dot_processed_sentences):
    verb_tense_errors = 0
    # print("sssssssssssssssssskdsjfngjkdfngkjdfng")
    for sentence_index, sentence in enumerate(dot_processed_sentences):
        pos_tagged_sentence = pos_tag(word_tokenize(sentence))
        # print(pos_tagged_sentence)
        tag_sequence = []
        for tag_index, tag in enumerate(pos_tagged_sentence):
            if len(tag_sequence) == 0:
                if tag[1] in verbs:
                    tag_sequence.append(tag[1])
            else:
                if tag[1] in verbs_with_adverb:
                    tag_sequence.append(tag[1])
                else:
#                    print(tag_sequence)
                    if len(tag_sequence) == 4:
                        if (', ').join(tag_sequence) not in fourgram_rules:
                            verb_tense_errors += 1
                            # print(tag, 'not present in fourgram')
                            # print(pos_tagged_sentence)
                    elif len(tag_sequence) == 3:
                        if (', ').join(tag_sequence) not in trigram_rules:
                            verb_tense_errors += 1
                            # print(tag, 'not present in trigram')
                            # print(pos_tagged_sentence)
                    elif len(tag_sequence) == 2:
                        if (', ').join(tag_sequence) not in bigram_rules:
                            verb_tense_errors += 1
                            # print(tag, 'not present in bigram')
                            # print(pos_tagged_sentence)
                    elif len(tag_sequence) == 1:
                        if tag_sequence[0] not in unigram_rules:
                            verb_tense_errors += 1
                            # print(tag, 'not present in unigram')
                            # print(pos_tagged_sentence)
                    # Based on length of tag_sequence -  check in the rules of length
                    tag_sequence = []
                    if tag[1] == 'TO':
                        tag_sequence.append(tag[1])
        # print(tag_sequence)
        # print("--------------------------------")

    return verb_tense_errors
