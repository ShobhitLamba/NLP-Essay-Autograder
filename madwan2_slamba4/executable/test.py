# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 17:09:41 2018

@author: shobh
"""

file= open('C:\Users\shobh\Desktop\NLP-Project\madwan2_slamba4\outputresults.txt', 'r')
line_index = 0
score = []
for i in range(100):
    file_list = file.readline(i)
    
for line in file_list:
        if line_index != 0:
            line_list = line.split(';')
