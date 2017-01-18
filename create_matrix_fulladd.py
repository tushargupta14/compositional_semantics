# Script creates matrix for the fulladd model. All the matrix are for the full corpus 
# Input : source_derived_stats.csv
# Output : matrix A : source_word; B : suffix; C : derived_word 

import numpy as np
import json


def create_matrix_fulladd(path_to_files):

	# Loading all the dictionaries 

	source_pmi_dict = json.load(open(path_to_files+"source_pmi_350dim.json","rb+"))

        derived_pmi_dict = json.load(open(path_to_files+"derived_pmi_350dim.json","rb+"))
	affix_pmi_dict = json.load(open(path_to_files+"suffix_pmi_350dim.json","rb+"))
	print "Dictionary Loaded"
	
	word_file = open("source_derived_words_stats.csv","rb+")

	derived_C = []
	source_A = []
	affix_B = []
	defaulter = []	
	target_dir = "/home/du3/13CS30045/affix_final/plsr_new/fulladd_input/"
	count =0 
	for line in word_file: 
		
		words = line.split(",")
		affix = words[0]
		source_word = words[1]
		derived_word = words[3]
		
		if affix in affix_pmi_dict :
			if source_word in source_pmi_dict and derived_word in derived_pmi_dict:
				s_vec = source_pmi_dict[source_word] 
                                d_vec = derived_pmi_dict[derived_word]
				affix_vec= affix_pmi_dict[affix]

				derived_C.append(d_vec)
				source_A.append(s_vec)
				affix_B.append(affix_vec)
				
		else :
			defaulter.append(affix)	

		count+=1
		if count%100 ==0 :
			print count 

	derived_C = np.array(derived_C,dtype = np.float32)
        source_A = np.array(source_A,dtype = np.float32)
        affix_B = np.array(affix_B,dtype = np.float32)
	
	print derived_C.shape,source_A.shape,affix_B.shape
	
	np.save(target_dir+'fulladd_source_350_A.npy',source_A)
        np.save(target_dir+'fulladd_derived_350_C.npy',derived_C)
	np.save(target_dir+'fulladd_affix_350_B.npy',affix_B)
	
	print defaulter

if __name__ == "__main__" :
	
	create_matrix_fulladd("/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files/")

	

	
				
