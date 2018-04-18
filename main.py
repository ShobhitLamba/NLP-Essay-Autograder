# author: Shobhit Lamba

from spelling import spellcheck  
      
def final_score(part_a, part_b, part_c_i, part_c_ii):
    #considering part_c_iii, part_d_i and part_d_ii to be zero for part 1 of project
    return 2 * part_a - part_b + part_c_i + part_c_ii

if __name__ == '__main__':
    csv_file = open(r'essays_dataset\index.csv', 'r')
    line_index = 0
    total_essay = [0, 0] 
    spellings = []
    grade = [] # 'high' or 'low'
    
    for line in csv_file:
        if line_index != 0:
            line_list = line.split(';')
            filepath = 'essays_dataset/essays/' + line_list[0]
            
            ''' Read file '''
            essay_file = open(filepath, 'r')
            one_essay = essay_file.read()
            
            part_b = spellcheck(one_essay)
            if line_list[2].strip().lower() == 'low':
                # print('low')
                total_essay[0] += 1
                spellings.append(part_b)
                grade.append('low')
            else:
                # print('High')
                total_essay[1] += 1
                spellings.append(part_b)
                grade.append('high')
            essay_file.close()
            if line_index == 1:
                # break
                pass
        
        line_index += 1

    csv_file.close()
