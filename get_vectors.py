import json
import csv

from collections import defaultdict


def get_words(path_to_vector_files):


        i=0
	word_list_dict = defaultdict(set)
        with open("../lazaridou/18ksouder.csv","rb+") as f :
                reader = csv.reader(f)
                for row in reader :
                        word_list_dict[row[2]].add(row[1])
        out_file = open("vector_lazaridou.txt","a")
        out_file1 = open("fastText_input.txt","a")
     
        for k,v in word_list_dict.iteritems():
                print k,v
        for key,values in word_list_dict.iteritems():

                out_file1.write(key+"\n")

                for value in values:
                        out_file1.write(value+"\n")
                        

if __name__ == "__main__" :

        get_words("../lazaridou/create_vectors/data_files/") 
