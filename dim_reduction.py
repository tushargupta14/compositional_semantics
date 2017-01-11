## Script applies Non-negative matrix factorization to the vectors obtained as PMI values 

import numpy as np 
import json 
import nimfa
import json
import cPickle as cp 
def generate_row_matrix_from_vectors(context_word_list,vec):

        X = []

        X = [vec[word] if word in vec else 0 for word in context_word_list ]
        #derived_Y = [d_vec[word] if word in d_vec else 0 for word in context_word_list]
        return X


def create_matrix(path_to_csv_files,path_to_json_files):
	
	context_file = open(path_to_csv_files+"context_word.csv")
        context_word_list = [line.split(",")[0] for line in context_file]

	context_file.close()

	R = [] ## vector matrix 

	count = 0
        pmi_dict = json.load(open(path_to_json_files+"pmi_values.json","rb+"))
	print "Dictionary Loaded"
	
	word_list = []
	count =0
	for key,vector in pmi_dict.iteritems():
	
		word_list.append(key)
		if count%100 == 0 :
			print count
		R.append(generate_row_matrix_from_vectors(context_word_list,vector))
		count+=1

	#R_array = np.asarray(R,dtype=np.float32)
	#print "Shape of the matrix created",R_array.shape
	#np.savetxt(path_to_csv_files+"vector_matrix.csv",R_array,delimiter=",")
	#with open(path_to_json_files+"vector_matrix.json","wb+") as outfile:
		#json.dump(R,outfile)
	#print "Json Dumped"
	#with open(path_to_json_files+"vector_matrix.pkl","wb+") as outfile:
		#cp.dump(R,outfile)
	#print "Pickle Dumped"
	return word_list,R

def non_negative_factorization(path_to_json_files,path_to_csv_files,word_list,R):

	## Read the file here 
	#R_array = np.array(R,dtype = np.float32)
	rank = 350
	print "Length of word list",len(word_list)
	nmf = nimfa.Nmf(R, rank=rank, seed='random_vcol', max_iter=100, 
                update='divergence', objective='div', n_run=50, track_factor=True)
	nmf_fit = nmf()
	

if __name__ == "__main__" :

	word_list,R = create_matrix("/home/du3/13CS30045/affix_final/lazaridou/csv/","/home/du3/13CS30045/affix_final/lazaridou/dictionaries/")

	non_negative_factorization("/home/du3/13CS30045/affix_final/lazaridou/dictionaries/","/home/du3/13CS30045/affix_final/lazaridou/csv/",word_list,R)
