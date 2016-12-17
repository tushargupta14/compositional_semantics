import os
import sys
import numpy as np
from collections import defaultdict
import math
import matplotlib.pyplot as plt

set_tags_to_keep = set(["CD","JJ","JJR","JJS","NN","NNS","NNP","NNPS","RB","RBR","RBS","UH","VB","VBD","VBG","VBN","VBP","VBZ"])
'''
Description: function to read context words
Input: path <path to folder containing context words>
Output: 
i) set_context_words, dict_word_count
'''

'''
Description: function to read context words
Input: path <path to folder containing context words>
Output: 
i) set_context_words, dict_word_count
'''

'''
Description: function to read context words
Input: path <path to folder containing context words>
Output: 
i) set_context_words, dict_word_count
'''


'''
Description: function to read context words
Input: path <path to folder containing context words>
Output: 
i) set_context_words, dict_word_count
'''

'''
Description: function to read context words
Input: path <path to folder containing context words>
Output: 
i) set_context_words, dict_word_count
'''

def read_context_words(path_to_context_words):
    set_context_word_count = set()
    set_word_count = set()
    
    j = 0
    
    # reading the tags from file. if the tags are in tags_to_keep then appending the count of the word
    with open(path_to_context_words + "pos_tag_dictionary.csv") as fp:
        
        for line in fp:
            print j
            j += 1
            temp = defaultdict(int)
            row = line.split('|')
            temp['word'] = row[0]
            tags = row[1].split(',')
            for i in tags:
                if i in set_tags_to_keep:
                    temp['count'] += 1
            set_word_count.add((temp['word'], temp['count']))
            
    #writing word count to file
    fp = open(path_to_context_words + "word_count.csv", "wb+")
    
    for i in set_word_count:
        fp.write(i[0] + "," + str(i[1]) + "\n")
    fp.close()
    
    
#     j = 0
#     for i in set_word_count:
#         print j
#         j += 1
#         temp = defaultdict(int)
#         temp['word'] = k
#         for i in v[0]:
#             if i in set_tags_to_keep:
#                 temp['count'] += 1
#         list_word_count.append(temp)
    
    
    # creating 
    default_dict_freq_count = defaultdict(int)
    for i in set_word_count:
        default_dict_freq_count[i[1]] += 1
    list_freq = list(default_dict_freq_count.keys())
    len_list_freq = len(list_freq)
    
    
    #keys
    sorted_list_freq = sorted(list_freq)
    
    #values
    sorted_list_count = [default_dict_freq_count[sorted_list_freq[i]] for i in xrange(len_list_freq)]
    
    count = 0
    index = None
    for i in xrange(len_list_freq):
        count += sorted_list_count[len_list_freq - 1 - i]
        if count > 40000:
            index = len_list_freq - 1 - i
            break
    
    threshold_freq = sorted_list_freq[index]
    
    for i in set_word_count:
        if i[1] > threshold_freq:
            set_context_word_count.add((i[0], i[1]))
    
    fp = open("context_word.csv", "wb+")
    j = 0
    for i in set_context_word_count:
        j += 1
        if j < 5:
            print i[0], i[1]
        fp.write(str(i[0]) + "," + str(i[1]) + "\n")
    fp.close()
        
    return set_context_word_count, set_word_count


if __name__ == "__main__" :

	read_context_words("/home/du3/13CS30045/lazaridou/")
