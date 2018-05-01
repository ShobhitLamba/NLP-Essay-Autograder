# author: Shobhit Lamba, Mohit Adwani

from sentence import count_sentences
from spelling import spellcheck
from grammar import subjectVerbAgreement
from verb_tense import verb_tense
from sentence_formation import check_sentence_formation
from topic_coherence import topic_coherence
#import nltk

# nltk.download('wordnet')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('treebank')
''' Wrapper for stanford corenlp '''
from stanfordcorenlp import StanfordCoreNLP
'''
Need to run the server before executing this
Refer - https://stanfordnlp.github.io/CoreNLP/corenlp-server.html
'''
nlp = StanfordCoreNLP('http://localhost',port=9000)
# nlp = StanfordCoreNLP(r'C:\Academic\NLP\stanford-corenlp-full-2018-02-27')

''' To calculate the final score of the essay '''
def final_score(part_a, part_b, part_c_i, part_c_ii, part_c_iii, part_d_ii):
    # considering part_c_iii, part_d_i and part_d_ii to be zero for part 1 of project
#     return 2 * part_a - part_b + part_c_i + part_c_ii + 2 * part_c_iii + 3 * part_d_ii
    # After using linear regression to optimize coefficients.
    return 0.44407603 * part_a - 0.20066031 * part_b + 0.11946078 * part_c_i - 0.08340117 * part_c_ii + 0.05725546 * part_c_iii + 0.05161766 * part_d_ii


if __name__ == '__main__':
    csv_file = open(r'../input/training/index.csv', 'r')
    line_index = 0
    total_essay = [0, 0]
    spellings = []
    spellings_N = []
    grades = [] # 'high' or 'low'
    essay_lengths = []
    essay_lengths_N = []
    essay_lengths_score = []
    sentences = []
    c_i_errors = []
    c_i_errors_N = []
    c_i_score = []
    c_ii_errors = []
    c_ii_errors_N = []
    c_ii_score = []
    topic_relevance = []
    topic_relevance_N = []

    c_iii_errors = []
    c_iii_errors_N = []
    c_iii_score = []

    part_a = 0
    part_b = 0
    part_c_i_error = 0
    part_c_ii_error = 0
    part_c_iii_error = 0
    part_d_ii = 0

''' Read training essays based on the sequence in the csv file '''
    for line in csv_file:
        if line_index != 0:
            line_list = line.split(';')
            filepath = '../input/training/essays/' + line_list[0]

            ''' Read file '''
            essay_file = open(filepath, 'r')
            one_essay = essay_file.read()

            # part_a = count_sentences(one_essay)
            ''' Count the number of sentences  '''
            part_a, dot_processed_sentences = count_sentences(one_essay, nlp)

            ''' count spelling mistakes '''
            part_b = spellcheck(one_essay)
            essay_lengths.append(part_a)
            spellings.append(part_b)
            part_c_i_error = subjectVerbAgreement(one_essay, nlp)

            c_i_errors.append(part_c_i_error)

            part_c_ii_error = verb_tense(dot_processed_sentences)

            c_ii_errors.append(part_c_ii_error)

            part_c_iii_error = check_sentence_formation(dot_processed_sentences, nlp)

            c_iii_errors.append(part_c_iii_error)

            part_d_ii = topic_coherence(one_essay, line_list[1])
            topic_relevance.append(part_d_ii)

            if line_list[2].strip().lower() == 'low':
                # print('low')
                total_essay[0] += 1
                grades.append('low')
            else:
                # print('High')
                total_essay[1] += 1
                grades.append('high')
            essay_file.close()
            print("Done with essay ", line_list[0],' ---', line_index)

        if line_index == 100:
            # exit()
            # break
            pass

        line_index += 1

    # Normalizing the scores to 0-1 scale
    for i in range(100):
        if spellings[i] == 0:
            spellings_N.append(0)
        else:
            spellings_N.append((spellings[i] - min(spellings)) / (max(spellings) - min(spellings)))
        essay_lengths_N.append((essay_lengths[i] - min(essay_lengths)) / (max(essay_lengths) - min(essay_lengths)))
        c_i_errors_N.append((c_i_errors[i] - min(c_i_errors)) / (max(c_i_errors) - min(c_i_errors)))
        c_ii_errors_N.append((c_ii_errors[i] - min(c_ii_errors)) / (max(c_ii_errors) - min(c_ii_errors)))
        c_iii_errors_N.append((c_iii_errors[i] - min(c_iii_errors)) / (max(c_iii_errors) - min(c_iii_errors)))
        topic_relevance_N.append((topic_relevance[i] - min(topic_relevance)) / (max(topic_relevance) - min(topic_relevance)))

    # Normalizing the scores to the required scale
    for i in range(100):
        spellings_N[i] *= 4
        spellings_N[i] = round(spellings_N[i])
        if c_i_errors_N[i] == 5:
            c_i_score.append(1)
        else:
            c_i_score.append(round(5 - 4 * c_i_errors_N[i]))

        if c_ii_errors_N[i] == 5:
            c_ii_score.append(1)
        else:
            c_ii_score.append(round(5 - 4 * c_ii_errors_N[i]))

        if c_iii_errors_N[i] == 5:
            c_iii_score.append(1)
        else:
            c_iii_score.append(round(5 - 4 * c_iii_errors_N[i]))

        if essay_lengths_N[i] == 5:
            essay_lengths_score.append(1)
        else:
            essay_lengths_score.append(round(5 - 4 * essay_lengths_N[i]))
        topic_relevance_N[i] *= 4
        topic_relevance_N[i] = round(topic_relevance_N[i]) + 1

    a = essay_lengths_score
    b = spellings_N
    c_i = c_i_score
    c_ii = c_ii_score
    c_iii = c_iii_score
    d_ii = topic_relevance_N

    part_i_final_scores = []
    for i in range(100):
        part_i_final_scores.append(final_score(a[i], b[i], c_i[i], c_ii[i], c_iii[i], d_ii[i]))

    csv_file.close()

# exit() # comment this before submitting

test_csv_file = open(r'../input/testing/index.csv', 'r')
results = open('../output/results.txt', 'w')
# firstline = True
test_a = 0
test_b = 0
test_c_i = 0
test_c_ii = 0
test_c_iii = 0
test_d_ii = 0
i = 0
test_line_index = 0

''' Read test essays and write the values in results.txt'''
for line in test_csv_file:
    if test_line_index != 0:
        line_list = line.split(';')
        filepath = '../input/testing/essays/' + line_list[0]

        ''' Read file '''
        essay_file = open(filepath, 'r')
        one_essay = essay_file.read()

        # part_a = count_sentences(one_essay)
        part_a, dot_processed_sentences = count_sentences(one_essay, nlp)
        part_b = spellcheck(one_essay)
        part_c_i_error = subjectVerbAgreement(one_essay, nlp)
        part_c_ii_error = verb_tense(dot_processed_sentences)
        part_c_iii_error = check_sentence_formation(dot_processed_sentences, nlp)
        part_d_ii = topic_coherence(one_essay, line_list[1])

        test_a = (part_a -  min(essay_lengths)) / (max(essay_lengths) - min(essay_lengths))
        test_b = (part_b - min(spellings)) / (max(spellings) - min(spellings))
        test_c_i = (part_c_i_error - min(c_i_errors)) / (max(c_i_errors) - min(c_i_errors))
        test_c_ii = (part_c_ii_error - min(c_ii_errors)) / (max(c_ii_errors) - min(c_ii_errors))
        test_c_iii = (part_c_iii_error - min(c_iii_errors)) / (max(c_iii_errors) - min(c_iii_errors))
        test_d_ii = (part_d_ii - min(topic_relevance)) / (max(topic_relevance) - min(topic_relevance))

        test_b *= 4
        test_b = round(test_b)
        test_d_ii *= 4
        test_d_ii = round(test_d_ii) + 1
        if test_c_i == 5:
            test_c_i = 1
        else:
            test_c_i = round(5 - 4 * test_c_i)

        if test_c_ii == 5:
            test_c_ii = 1
        else:
            test_c_ii = round(5 - 4 * test_c_ii)

        if test_c_iii == 5:
            test_c_iii = 1
        else:
            test_c_iii = round(5 - 4 * test_c_iii)

        if test_a == 5:
            test_a = 1
        else:
            test_a = round(4 * test_a) + 1

        test_final_score = final_score(test_a, test_b, test_c_i, test_c_ii, test_c_iii, test_d_ii)

        results.write(line_list[0])
        results.write(";")
        results.write(str(test_a))
        results.write(";")
        results.write(str(test_b))
        results.write(";")
        results.write(str(test_c_i))
        results.write(";")
        results.write(str(test_c_ii))
        results.write(";")
        results.write(str(test_c_iii))
        results.write(";0;")
        results.write(str(test_d_ii))
        results.write(";")
        results.write(str(test_final_score))
        results.write(";")
        # Keeping the dividing point for high and low at 1.87 which is the midpoint of final scores
        if test_final_score >= 1.87:
            results.write("high\n")
        else:
            results.write("low\n")

        print("Done with test essay ", line_list[0])

    test_line_index += 1

test_csv_file.close()
results.close()
nlp.close()
