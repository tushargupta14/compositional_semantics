## Script applies Non-negative matrix factorization to the vectors obtained as PMI values 
## Need to chnage in the scrpit whether to obtain for source words , derived words or for suffixes
import numpy as np 
import json 
import nimfa
import json
import cPickle as cp
from sklearn.decomposition import NMF
 
def generate_row_matrix_from_vectors(context_word_list,vec):

        X = []

        X = [vec[word] if word in vec else 0 for word in context_word_list ]
        #derived_Y = [d_vec[word] if word in d_vec else 0 for word in context_word_list]
        return X


def create_matrix(path_to_files):
	
	context_file = open(path_to_files+"context_word.csv")
        context_word_list = [line.split(",")[0] for line in context_file]

	context_file.close()

	R = [] ## vector matrix 

	count = 0
	print "Loading Dictionary"
        suffix_pmi_dict = json.load(open(path_to_files+"suffix_pmi.json","rb+")) ## 2 changes
	print "Dictionary Loaded"
	
	word_list = []
	count =0
	for key,vector in suffix_pmi_dict.iteritems():    ## change here 
	
		word_list.append(key)
		if count%100 == 0 :
			print count
		R.append(generate_row_matrix_from_vectors(context_word_list,vector))
		count+=1
	non_negative_factorization(path_to_files,word_list,R)

	

def non_negative_factorization(path_to_files,word_list,R):

	## Read the file here 
	R_array = np.array(R,dtype = np.float32)
	rank = 350
	print "Length of word list",len(word_list)
	
	model = NMF(n_components=350, init='random', random_state=0)
	
	print "Fitting the model"
	W = model.fit_transform(R_array)

	H = model.components_

## Changes in the name of files 
	print "Writing to files"
	np.savetxt(path_to_files+"W_suffixes.txt",W)
	np.savetxt(path_to_files+"H_suffixes.txt",H)
	
	return W,H
if __name__ == "__main__" :

	word_list,R = create_matrix("/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files/")

	W,H = non_negative_factorization("/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files/",word_list,R)
