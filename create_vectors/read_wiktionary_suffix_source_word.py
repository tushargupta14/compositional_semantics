import os
import sys
import numpy as np
from collections import defaultdict
import math
import matplotlib.pyplot as plt
import json

'''
Description: function to read content words, suffixes and target words from files in folder given by path
Input: path <path to folder containing suffix files>
suffix files are named as "-<suffix>" eg. -age, -ly etc.
the files are csv with each row as "<wiktionary link to the derived word>,<derived word>,<source word>,<suffix>"
Output: 
i) dict_context_words (a dictionary with the affix as key, and a list of words containing that affix, as value)
ii) set_source_words (a set of all source words)
iii) set_suffixes (a set of all suffixes)
'''


def read_wiktionary_suffix_source_word(path_to_suffix_list):
    
    
    files = os.listdir(path_to_suffix_list)
    
    # initialize return values
    dict_suffix_derived_words = defaultdict(set)
    set_suffixes = set()
    set_derived_words = set()
    set_source_words = set()
    
    count = 0
    corrupt = 0
    for f in files:
        
        
        # in file suffix is stored as "-<suffix" eg. "-age", "-ly". Removing the "-"
        suffix = f[1:]
        dict_suffix_derived_words[suffix] = []
        set_suffixes.add(suffix)
        
        with open(path_to_suffix_list + f) as fp:
            for line in fp:
                count += 1
                row = line.split(',')
                
                
                # row is corrupt, ignore the row
                if len(row) < 4:
                    corrupt += 1
                    continue
                
                
                dict_suffix_derived_words[suffix].append(row[1])
                set_source_words.add(row[2])
                set_derived_words.add(row[1])
        print count, corrupt
    fp = open("suffixes.csv", "wb+")
    
    for i in set_suffixes:
        fp.write(i + "\n")
    
    fp.close()
    
    fp = open("source_words.csv", "wb+")
    
    for i in set_source_words:
        fp.write(i + "\n")
    fp.close()
    
    fp = open("derived_words.csv", "wb+")
    
    for i in set_derived_words:
        fp.write(i + "\n")
    fp.close()
    
    
    fp = open("suffix_derived_words.json", "wb+")
    json.dump(dict_suffix_derived_words, fp)
    fp.close()
    return dict_suffix_derived_words, set_suffixes, set_source_words, set_derived_words



if __name__ == "__main__":
		
	read_wiktionary_suffix_source_word("/home/du3/13CS30045/affix_final/wiktionary/results_dec_2/")
