# Creates dictioanry for the 350 dimensional vectors
import numpy as np
import json

"""def generate_vector(word_array):

	
	counter =0 
	vector = []
	for value in word_array :
		
		vector_dict[] = value
			counter+=1

	return vector_dict
				
"""

def create_word_list(path_to_files):

	#context_file = open(path_to_files+"context_word.csv")
        #context_word_list = [line.split(",")[0] for line in context_file]

        #context_file.close()
	
	suffix_word_list = []
	derived_word_list = []
	source_word_list = []
	suffix_pmi_dict = json.load(open(path_to_files+"suffix_pmi.json","rb+"))
	print "Here"	 	
	suffix_word_list = [key for key in suffix_pmi_dict.iterkeys()]
	
	#source_pmi_dict = json.load(open(path_to_files+"source_word_pmi.json"))
	print "Here"
	#source_word_list = [key for key in source_pmi_dict.iterkeys()]
	
	#derived_pmi_dict = json.load(open(path_to_files+"derived_words_pmi.json"))
	print "Here"
	#derived_word_list = [key for key in derived_pmi_dict.iterkeys()]


	return suffix_word_list,source_word_list,derived_word_list



def create_dictionary(path_to_files):
		

	suffix_word_list,source_word_list,derived_word_list = create_word_list(path_to_files)

	context_file = open(path_to_files+"context_word.csv")
        context_word_list = [line.split(",")[0] for line in context_file]
        context_file.close()
	"""
	##### Source Word #####

	print len(source_word_list)
	W = np.genfromtxt(path_to_files+"W_source.txt")
	print W.shape


	red_source_word_dict = {}
	for i in xrange(len(source_word_list)):
	
		red_source_word_dict[source_word_list[i]] = W[i].tolist()
		print i,len(source_word_list)
				
	with open(path_to_files+"source_pmi_350dim.json","wb+") as f:
		json.dump(red_source_word_dict,f)"""
	"""
	#### Derived Words #### 

	print len(derived_word_list)
        W = np.genfromtxt(path_to_files+"W_derived.txt")
        print W.shape


        red_derived_word_dict = {}
        for i in xrange(len(derived_word_list)):

                red_derived_word_dict[derived_word_list[i]] = W[i].tolist()
                print i,len(derived_word_list)

        with open(path_to_files+"derived_pmi_350dim.json","wb+") as f:
                json.dump(red_derived_word_dict,f)
	"""
  	## Suffix Words 


	print len(suffix_word_list)
        W = np.genfromtxt(path_to_files+"W_suffixes.txt")
        print W.shape


        red_suffix_word_dict = {}
        for i in xrange(len(suffix_word_list)):

                red_suffix_word_dict[suffix_word_list[i]] = W[i].tolist()
                print i,len(suffix_word_list)

        with open(path_to_files+"suffix_pmi_350dim.json","wb+") as f:
                json.dump(red_suffix_word_dict,f)
	

		
if __name__ == "__main__":
	
	create_dictionary("/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files/")
