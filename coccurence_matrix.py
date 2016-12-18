# File createss a co occurence matrix for the source and derived words
# Input : source_words_with_counts.csv, derived_words_with_counts.csv, context_words.csv 
# Output : co-occurence representation target word context word count 
# 2 dictionaries : source_co_occurence_matrix.json and derived_co_occurence_matrix.json
# A 2 level dictionary with key as the word , secondary key as the context word and value is the corresponding count
import json 
from collections import defaultdict

def co_occurence_matrix_suffixes(path_to_files) :

# Builds the co_occurence matrix for the suffiexs 
# Takes input suffix_dict_with_counts.json
	dict_co_occurence_suffix_context_word_adjacency_list = defaultdict(lambda: defaultdict(int))
	input_file = open(path_to_files+"suffix_dict_with_counts.json","rb+")
	suffix_dict = json.load(input_file)
	input_file.close()
	count =0
	print "Suffix Dict loaded"

	fp1 = open(path_to_files+"derived_co_occurence_matrix.json","rb+")
	dict_co_occurence_derived_word_context_word_adjacency_list = json.load(fp1)
	fp1.close()

	print "Derived word dict loaded"
	for suffix,derived_list in suffix_dict.iteritems() : 
        	for derived_word in derived_list:

			try :
            			for k,v in dict_co_occurence_derived_word_context_word_adjacency_list[derived_word[0]].iteritems():
			
             	   			dict_co_occurence_suffix_context_word_adjacency_list[suffix][k] += int(v)
			except KeyError : 
				# the derived was not present orignally in wiktioanry so didnot come into the suffix_dict_derived_words but i spresent in the corpus . 
				print "keyerror",derived_word
		count+=1
		print count
	print len(dict_co_occurence_derived_word_context_word_adjacency_list)
	
	out_file = open("suffix_co_occurence_matrix.json","wb+")
	json.dump(dict_co_occurence_suffix_context_word_adjacency_list,out_file)
	out_file.close()



def co_occurence_matrix(path_to_files) :


    # Computes the matrix for only source and derived words
    # making two level defaultdict with primary keys as rows and secondary keys as columns
    dict_co_occurence_source_word_context_word_adjacency_list = defaultdict(lambda: defaultdict(int))
    #dict_co_occurence_suffix_context_word_adjacency_list = defaultdict(lambda: defaultdict(int))
    dict_co_occurence_derived_word_context_word_adjacency_list = defaultdict(lambda: defaultdict(int))
   
    
    with open(path_to_files+"source_list_with_counts.csv") as f :
	set_source_words = set()
	set_source_words = { line.split(",")[0] for line in f}
    with open(path_to_files+"derived_list_with_counts.csv") as f :
	set_derived_words = set()
	set_derived_words = { line.split(",")[0] for line in f }
    
    with open(path_to_files+"context_word.csv") as f :
        set_context_words = set()
        set_context_words = { line.split(",")[0] for line in f }    


    print len(set_source_words),len(set_derived_words)
	
    

    total_word_count = 0
    int_window_size = 2 

    count = 0 	
    with open("/home/du3/13CS30045/datasets/enwiki/enwiki_cleaned.txt","rb+") as corpus:
#         last_row = [None for i in xrange(2*int_window_size)]
        for line in corpus:
            row = line.split()
            row = [None, None] + row + [None, None]
            len_row = len(row)
            
            
            total_word_count += len_row - int_window_size*2
            
	    count+=1

            if count%100==0 :
		 print count  
            #print count
	    continue   

            ######## 
            for i in xrange(int_window_size, len_row - int_window_size):
                
                if row[i] not in set_source_words and row[i] not in set_derived_words:
                    continue
                else:
                    
                    
                    for j in xrange(i - int_window_size, i + int_window_size + 1):


                        if j == i:
                            continue
                        else:
                            if row[j] in set_context_words:
                                if row[i] in set_source_words:
                                    dict_co_occurence_source_word_context_word_adjacency_list[row[i]][row[j]] += 1
                                elif row[i] in set_derived_words:
                                    dict_co_occurence_derived_word_context_word_adjacency_list[row[i]][row[j]] += 1
                                else:
                                    print "Error: ", row[i]
                                    continue
	 
	print total_word_count,"total-word_count"
   
     	#fp = open("source_co_occurence_matrix.json","wb+")  	         
     	#json.dump(dict_co_occurence_source_word_context_word_adjacency_list,fp)
	
     	#fp.close()

     	#fp = open("derived_co_occurence_matrix.json","wb+")
     	#json.dump(dict_co_occurence_derived_word_context_word_adjacency_list,fp) 
     	#fp.close()
	
	#print len(dict_co_occurence_derived_word_context_word_adjacency_list),len(dict_co_occurence_source_word_context_word_adjacency_list)

if __name__ == "__main__" :

	co_occurence_matrix("/home/du3/13CS30045/lazaridou/")
    	



