# author: Shobhit Lamba

from mohit_main import count_sentences
from spelling import spellcheck  
from grammar import subjectVerbAgreement
      
def final_score(part_a, part_b, part_c_i, part_c_ii):
    #considering part_c_iii, part_d_i and part_d_ii to be zero for part 1 of project
    return 2 * part_a - part_b + part_c_i + part_c_ii

if __name__ == '__main__':
    csv_file = open(r'essays_dataset\index.csv', 'r')
    line_index = 0
    total_essay = [0, 0] 
    spellings = []
    grades = [] # 'high' or 'low'
    essay_lengths = []
    sentences = []
    c_i_errors = []
    for line in csv_file:
        if line_index != 0:
            line_list = line.split(';')
            filepath = 'essays_dataset/essays/' + line_list[0]
            
            ''' Read file '''
            essay_file = open(filepath, 'r')
            one_essay = essay_file.read()
            
            part_a = count_sentences(one_essay)
            part_b = spellcheck(one_essay)
            essay_lengths.append(part_a)
            spellings.append(part_b)
            part_c_i = subjectVerbAgreement(one_essay)
#            for sentence in sentences:
#                part_c_i += subjectVerbAgreement(sentence)
            
            c_i_errors.append(part_c_i)
            
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
        
        line_index += 1

    csv_file.close()
