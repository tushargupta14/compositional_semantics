import json
from collections import defaultdict



def create_dictionaries(path_to_files):

        print "Creating Dictionaries"
        count = 0
        source_fastText_dict = defaultdict(list)
        with open(path_to_files+"source_fastText_output.txt","r") as source_file:
                for line in source_file :
                        vector = []
                        vector = [value for value in line.rstrip().split(" ")]
                        source_word = vector[0]
                        source_fastText_dict[source_word] = vector[1:]
                        count+=1
                        print count,len(vector)
        derived_fastText_dict = defaultdict(list)

        count =0
        with open(path_to_files+"derived_fastText_output.txt","rb+") as source_file:
                for line in source_file :
                        vector = []
                        vector = [value for value in line.rstrip().split(" ")]

                        derived_word = vector[0]
                        derived_fastText_dict[derived_word] = vector[1:]
                        count+=1
                        print count, len(vector)

        affix_fastText_dict = defaultdict(list)
        count = 0
        with open(path_to_files+"affix_fastText_output.txt","rb+") as source_file:
                for line in source_file :
                        vector = []
                        vector = [value for value in line.rstrip().split(" ")]

                        affix_word = vector[0]
                        affix_fastText_dict[affix_word] = vector[1:]
                        count+=1
                        print count, len(vector)

        with open(path_to_files+"source_fastText_350dim.json","wb+") as f:
                json.dump(source_fastText_dict,f)
        with open(path_to_files+"derived_fastText_350dim.json","wb+") as f:
                json.dump(derived_fastText_dict,f)
                                                  


if __name__ == "__main__"  : 

	create_dictionaries("/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files/")    
