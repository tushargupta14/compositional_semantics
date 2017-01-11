# Script for creating context_words.csv for top N occuring context words 
# Input : Input: path <path to folder containing pos_tag dictioanry> and the dimension of the vectors 

import os
import sys
import numpy as np
from collections import defaultdict
import math
import matplotlib.pyplot as plt
import json

def read_context_words(path_to_pos_tags,dimension):

	set_tags_to_keep = set(["CD","JJ","JJR","JJS","NN","NNS","NNP","NNPS","RB","RBR","RBS","UH","VB","VBD","VBG","VBN","VBP","VBZ"])

	j=0 
	set_context_word_count = set()
    	set_word_count = set()
    	
	with open(path_to_pos_tags + "pos_tag_dictionary.csv") as fp:
        	
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
    	fp = open( "word_count.csv", "wb+")
    
    	for i in set_word_count:
        	fp.write(i[0] + "," + str(i[1]) + "\n")
    	fp.close()

	default_dict_freq_count = defaultdict(int)
    	for i in set_word_count:
        	default_dict_freq_count[i[1]] += 1
    	list_freq = list(default_dict_freq_count.keys())
    	len_list_freq = len(list_freq)
	
	sorted_list_freq = sorted(list_freq)

	sorted_list_count = [default_dict_freq_count[sorted_list_freq[i]] for i in xrange(len_list_freq)]
	
	count = 0
    	index = None
    	for i in xrange(len_list_freq):
        	count += sorted_list_count[len_list_freq - 1 - i]
        	if count > dimension:
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

	#return set_context_word_count, set_word_count


if __name__ == "__main__" :
	

	read_context_words("/home/du3/13CS30045/affix_final/lazaridou/csv/",20000)
