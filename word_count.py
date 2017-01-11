import json
import os
import sys
from collections import defaultdict

def get_word_count(set_words_to_count, filename):
    count = defaultdict(int)
    i = 0
    with open(filename) as fp:
        for row in fp:
       	    print i, count['cross']
            i += 1
	    words = row.split(' ')
            for word in words:
                if word in set_words_to_count:
                    count[word] += 1
    return count


def get_set_word_from_json_file(filename):
    set_words = set()
    with open(filename) as fp:
        for row in fp:
            words = json.loads(row)
            if words['source_word'].isalpha() and words['derived_word'].isalpha():
                set_words.add(words['source_word'])
                set_words.add(words['derived_word'])
    return set_words

filename_words = "/home/du3/13CS30045/affix_final/lazaridou/able_minimal.json"
filename_corpus = "/home/du3/13CS30045/affix_final/datasets/enwiki/enwiki_cleaned.txt"
output_file = "/home/du3/13CS30045/affix_final/lazaridou/able_count.csv"


set_words_to_count = get_set_word_from_json_file(filename_words)
print len(set_words_to_count)

defaultdict_word_count = get_word_count(set_words_to_count, filename_corpus)

fp = open(output_file, "wb+")

for key, value in defaultdict_word_count.iteritems():
    fp.write(key + "," + str(value) + "\n")
fp.close()
