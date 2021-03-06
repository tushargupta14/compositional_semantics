# Script creates a imput matrix X for source words and a output matrix Y for derived words from the PMI scores 

# The script is used for the PLS method implemented in the lazaridou paper 
# Input : context word file, source words and derived words for a particular affix 

import numpy as np
import json
from convert_to_Rdata import *
def generate_suffix_row_matrix_from_vectors(context_word_list,s_vec):

	source_X = []

	source_X = [s_vec[word] if word in s_vec else 0 for word in context_word_list ]	
	#derived_Y = [d_vec[word] if word in d_vec else 0 for word in context_word_list]
	return source_X

def generate_derived_row_matrix_from_vectors(context_word_list,d_vec):

	derived_Y = []
	
	derived_Y = [d_vec[word] if word in d_vec else 0 for word in context_word_list]
	return derived_Y

def generate_affix_row_matrix_from_vectors(context_word_list,affix_vec):
	
	affix_U = []
		
	affix_U = [affix_vec[word] if word in affix_vec else 0 for word in context_word_list]

	return affix_U



	
def create_matrix_for_affix(path_to_files,source_pmi_dict,derived_pmi_dict,word_file,affix):

	# Take all the source words 
	# Take all the derived words 
	
	# Take all the context words 
	# Make a numpy array 

	#context_file = open(path_to_files+"context_word.csv")
	#context_word_list = [line.split(",")[0] for line in context_file]
	
	#dim = len(context_word_list)

	#context_file.close()

	word_file = open("source_derived_words_stats.csv","rb+")
	
	derived_Y = []
	source_X = []
	count = 0
  	#source_pmi_dict = json.load(open(path_to_files+"source_pmi_350dim.json","rb+"))

	#derived_pmi_dict = json.load(open(path_to_files+"derived_pmi_350dim.json","rb+"))
	print "Dictioanry loaded"
	
	target_dir = "/home/du3/13CS30045/affix_final/plsr_new/pls/data/lazaridou_lexfunc_model_input/"
	counter = 0
	for line in word_file :

		line_split = line.split(",")
		line_affix = line_split[0]
		
		if affix == line_affix :
			source_word = line_split[1]
			derived_word = line_split[3]
			
			if source_word in source_pmi_dict and derived_word in derived_pmi_dict:
				s_vec = source_pmi_dict[source_word]	
				d_vec = derived_pmi_dict[derived_word]
				source_X.append(s_vec) 
				derived_Y.append(d_vec)	
				count+=1	
		else :
			continue

	#print len(source_X[0]),count	
	source_X = np.array(source_X,dtype =np.float32)
	derived_Y = np.array(derived_Y,dtype = np.float32)
	#convert_to_Rdata(affix,source_X,derived_Y)

	np.save(target_dir+affix+'_source_350_X.npy',source_X)
	np.save(target_dir+affix+'_derived_350_Y.npy',derived_Y)
	#np.savetxt(target_dir+affix+'_source_350_X.txt',source_X)
	#np.savetxt(target_dir+affix+'_derived_350_Y.txt',derived_Y)
	#print affix,source_X.shape,derived_Y.shape
	print source_X

#create_matrix_fulladd():
	


if __name__ == "__main__" :

	create_matrix_for_affix("/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files/","able")
