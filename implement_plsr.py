# Script creates lexfunc matrices for affixes for lazaridou vectors. It is used as a wrapper for create_matrix.py

import sys
#sys.path.insert(0, '')

from create_matrix import *
import json 
from convert_to_Rdata import *
def wrapper_func(path_to_files):
	# Load the suffix list 
	# Iterate over it and create the matrix for each o0ne of them 
	## lOADING all the dictionary 
	"Loading dictioanries"

	suffix_dict = json.load(open(path_to_files+"suffix_pmi_350dim.json"))
	suffix_list = [key for key in suffix_dict.iterkeys()]
	
	word_file = open(path_to_files+"source_derived_words_stats.csv","rb+")	
	source_pmi_dict = json.load(open(path_to_files+"source_pmi_350dim.json","rb+"))
        derived_pmi_dict = json.load(open(path_to_files+"derived_pmi_350dim.json","rb+"))

	
	
        print "Dictioanry loaded"
	count =0
	for suffix in suffix_list:
		create_matrix_for_affix(path_to_files,source_pmi_dict,derived_pmi_dict,word_file,suffix)
		count+=1
		
		print suffix,count,len(suffix_list)
		
	

if __name__ == "__main__":

	path_to_files = "/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files/"

	wrapper_func(path_to_files)

