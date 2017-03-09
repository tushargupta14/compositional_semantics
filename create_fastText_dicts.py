## Script computes the fastText vectors for all the source words, derived words and affixes present in the corpus

import json
import csv
import subprocess 
from collections import defaultdict

def create_dictionaries(path_to_files):
	
	print "Creating Dictionaries"
	count = 0 
	source_fastText_dict = defaultdict(list)
	with open(path_to_files+"source_fastText_output.txt","rb+") as source_file:
		for line in source_file :
			vector = []
			vector = [value for value in line.rstrip().split(" ")]
			source_word = vector[0]
			for val in vector[1:]:
				source_fastText_dict[source_word].append(float(val))
			count+=1 
			print count
	derived_fastText_dict = defaultdict(list)
	
	count =0 
	with open(path_to_files+"derived_fastText_output.txt","rb+") as source_file:
                for line in source_file :
			vector = []
			vector = [value for value in line.rstrip().split(" ")]
                     
                        derived_word = vector[0]
			for val in vector[1:] :
		
                        	derived_fastText_dict[derived_word].append(float(val)) 
			count+=1
			print count, len(vector)

	affix_fastText_dict = defaultdict(list)
	count = 0
	with open(path_to_files+"affix_fastText_output.txt","rb+") as source_file:
                for line in source_file :
                        vector = []
                        vector = [value for value in line.rstrip().split(" ")]
				
                        affix_word = vector[0]
			for val in vector[1:]:
                        	affix_fastText_dict[affix_word].append(float(val))
                        count+=1
                        print count, len(vector)
	
	with open(path_to_files+"source_fastText_350dim.json","wb+") as f:
		json.dump(source_fastText_dict,f)	
	with open(path_to_files+"derived_fastText_350dim.json","wb+") as f:
                json.dump(derived_fastText_dict,f)
        
	with open(path_to_files+"affix_fastText_350dim.json","wb+") as f:
                json.dump(affix_fastText_dict,f)


def create_input_files(path_to_files):

	source_pmi_dict = json.load(open(path_to_files+"source_pmi_350dim.json","rb+"))
        derived_pmi_dict = json.load(open(path_to_files+"derived_pmi_350dim.json","rb+"))
	
	affix_pmi_dict = json.load(open(path_to_files+"suffix_pmi_350dim.json","rb+"))
	with open(path_to_files+"source_fastText_input.txt","wb+") as f:
		for keys in source_pmi_dict.iterkeys() :
			f.write(keys+"\n")
	with open(path_to_files+"derived_fastText_input.txt","wb+") as f:
		for keys in derived_pmi_dict.iterkeys() :
			f.write(keys+"\n")

	with open(path_to_files+"affix_fastText_input.txt","wb+") as f:
                for keys in affix_pmi_dict.iterkeys() :
                        f.write(keys+"\n")

	print "Input files created"
	#print_vectors(path_to_files)

	input_file = path_to_files+"source_fastText_input.txt"
	output_file1 = path_to_files+"source_fastText_output.txt"

        command = "cat " + input_file +" | ./fasttext print-vectors /home/du3/13CS30045/affix_final/datasets/enwiki/fasText_results/model7.bin > "+output_file1

        p = subprocess.Popen(command,cwd = "/home/du3/13CS30045/fastText",shell=True)
    
        p.communicate()


        print "source fastText finished."

        input_file = path_to_files+"derived_fastText_input.txt"
        output_file2 = path_to_files+"derived_fastText_output.txt"


        command = "cat " + input_file +" | ./fasttext print-vectors /home/du3/13CS30045/affix_final/datasets/enwiki/fasText_results/model7.bin > "+output_file2

        p = subprocess.Popen(command,cwd = "/home/du3/13CS30045/fastText",shell=True)
   
        p.communicate()

        print "fastText for derived words finished"



	input_file = path_to_files+"affix_fastText_input.txt"
        output_file3 = path_to_files+"affix_fastText_output.txt"

        command = "cat " + input_file +" | ./fasttext print-vectors /home/du3/13CS30045/affix_final/datasets/enwiki/fasText_results/model7.bin > "+output_file3

        p = subprocess.Popen(command,cwd = "/home/du3/13CS30045/fastText",shell=True)
	print "Affix fastText finished"
        p.communicate()


	#create_dicts(path_to_files)

if __name__ == "__main__" :
	
	#create_input_files("/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files/")
	create_dictionaries("/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files/")
