# author: Shobhit Lamba, Mohit Adwani

from sentence import count_sentences
from spelling import spellcheck
from grammar import subjectVerbAgreement
from verb_tense import verb_tense

import nltk

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('treebank')

def final_score(part_a, part_b, part_c_i, part_c_ii):
    # considering part_c_iii, part_d_i and part_d_ii to be zero for part 1 of project
    return 2 * part_a - part_b + part_c_i + part_c_ii


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

    part_a = 0
    part_b = 0
    part_c_i_error = 0
    part_c_ii_error = 0

    for line in csv_file:
        if line_index != 0:
            line_list = line.split(';')
            filepath = '../input/training/essays/' + line_list[0]

            ''' Read file '''
            essay_file = open(filepath, 'r')
            one_essay = essay_file.read()

            part_a = count_sentences(one_essay)
            part_a, dot_processed_sentences = count_sentences(one_essay)

            part_b = spellcheck(one_essay)
            essay_lengths.append(part_a)
            spellings.append(part_b)
            part_c_i_error = subjectVerbAgreement(one_essay)
#            for sentence in sentences:
#                part_c_i += subjectVerbAgreement(sentence)

            c_i_errors.append(part_c_i_error)

            # if line_index == 3:
            part_c_ii_error = verb_tense(dot_processed_sentences)
#            for sentence in sentences:
#                part_c_i += subjectVerbAgreement(sentence)
            c_ii_errors.append(part_c_ii_error)

            if line_list[2].strip().lower() == 'low':
                # print('low')
                total_essay[0] += 1
                grades.append('low')
            else:
                # print('High')
                total_essay[1] += 1
                grades.append('high')
            essay_file.close()
            print("Done with essay ", line_list[0])
            if line_index == 1:
                # break
                pass

        if line_index == 3:
            # break
            pass

        line_index += 1

    for i in range(100):
        if spellings[i] == 0:
            spellings_N.append(0)
        else:
            spellings_N.append((spellings[i] - min(spellings)) / (max(spellings) - min(spellings)))
        essay_lengths_N.append((essay_lengths[i] - min(essay_lengths)) / (max(essay_lengths) - min(essay_lengths)))
        c_i_errors_N.append((c_i_errors[i] - min(c_i_errors)) / (max(c_i_errors) - min(c_i_errors)))
        c_ii_errors_N.append((c_ii_errors[i] - min(c_ii_errors)) / (max(c_ii_errors) - min(c_ii_errors)))

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

        if essay_lengths_N[i] == 5:
            essay_lengths_score.append(1)
        else:
            essay_lengths_score.append(round(5 - 4 * essay_lengths_N[i]))

    a = essay_lengths_score
    b = spellings_N
    c_i = c_i_score
    c_ii = c_ii_score

    part_i_final_scores = []
    for i in range(100):
        part_i_final_scores.append(final_score(a[i], b[i], c_i[i], c_ii[i]))

    results = open('../output/results.txt', 'w')
    firstline = True
    i = 0
    for line in csv_file:
        if line_index != 0:
            line_list = line.split(';')
        if firstline:
            firstline = False
            continue
        else:
            results.write(line_list[0])
            results.write(";")
            results.write(str(a[i]))
            results.write(";")
            results.write(str(b[i]))
            results.write(";")
            results.write(str(c_i[i]))
            results.write(";")
            results.write(str(c_ii[i]))
            results.write(";0;0;0;unknown\n")
            i += 1

    results.close()
    csv_file.close()
