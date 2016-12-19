# Calculates the pmi score for a target word and stores in a dictionary with the respective context word
# Input all the *_co_occurence_matrix.json
# context_words.csv 
# derived_list_with_counts.csv 
# source_list_with_counts.csv 

import json  
from collections import defaultdict 
import math

def create_dict_word_count(path_to_files) :

	fp1 = open(path_to_files+"source_list_with_counts.csv")
	
	source_word_count = {}
	
	source_word_count = {line.split(",")[0]:int(line.split(",")[1].rstrip()) for line in fp1 }
	
	fp1 = open(path_to_files+"derived_list_with_counts.csv")
	derived_word_count = {}

	derived_word_count = {line.split(",")[0]:int(line.split(",")[1].rstrip()) for line in fp1 }
	fp1 = open(path_to_files+"context_word.csv") 
	context_word_count = {}
	context_word_count = {line.split(",")[0]:int(line.split(",")[1].rstrip()) for line in fp1}


	suffix_word_count = defaultdict(int)

	fp1 = open("suffix_dict_with_counts.json")

	suffix_dict = json.load(fp1)
		
	for suffix,derived_words in suffix_dict.iteritems():	
		for item in derived_words : 
			suffix_word_count[suffix]+= int(item[1])
	fp1.close()
	
	#print suffix_word_count 
	return source_word_count,derived_word_count,suffix_word_count,context_word_count 

	      

def cal_pmi(path_to_files):
	
	# Total word count
	# Create a final file containing all the derived words, source words and suffixes that ocuur with the context words
	total_word_count  = 962643860
	dict_pmi = defaultdict(lambda: defaultdict(int))
	
	log_file = open("defaulters.txt","wb+") ## Log file to write all defaulters 
	source_word_count,derived_word_count,suffix_word_count,context_word_count = create_dict_word_count(path_to_files)
	
	########################################## DERIVED WORDS ######################################################################
	derived_co_occurence_dict = json.load(open(path_to_files+"derived_co_occurence_matrix.json","rb+"))
	count =0 	
	for derived_word,ind_count in derived_word_count.iteritems():
		count+=1
		if ind_count == 0 :
			continue
		try :
                	for context_word, mutual_count in derived_co_occurence_dict[derived_word].iteritems():
				try :
                        		dict_pmi[derived_word][context_word] = max(math.log((float(mutual_count*total_word_count))/ind_count*context_word_count[context_word], 2),0)
				except Error as e :
					print "context_word error:",context_word
					log_file.write("{},{}+\n".format(e,context_word))
		except KeyError :
			log_file.write(derived_word+"\n")
			
		if count%100==0 :
			print "derived_words", count
	print "Pmi done for derived words"
	
	print len(dict_pmi)	
	############################################# SOURCE WORDS ##################################################################
	source_co_occurence_dict = json.load(open(path_to_files+"source_co_occurence_matrix.json","rb+"))
	count =0 
	print "Loaded source words dict"
	for source_word,ind_count in source_word_count.iteritems():
		count+=1 
		if ind_count ==0 :
			continue
		try :
                	for context_word, mutual_count in source_co_occurence_dict[source_word].iteritems():
				try :
                        		dict_pmi[source_word][context_word] = max(math.log((float(mutual_count*total_word_count))/ind_count*context_word_count[context_word], 2), 0)
				except Error as e :
					print "context_word error:",context_word
                                        log_file.write("{},{}+\n".format(e,context_word))
					
		except Error as e :
			log_file.write(source_word+"\n")

		if count%100 ==0 :
			print count,"source_word"
	print "PMI DOne for source words"
	
	################################################# SUFFIXES #####################################################################

	suffix_co_occurence_dict = json.load(open(path_to_files+"suffix_co_occurence_matrix.json","rb+"))
	print "Loaded suffix words dict"	
	count =0 
	for suffix,ind_count in suffix_word_count.iteritems():
		count+=1 
		if ind_count == 0 :
			continue
		try :	
		 	for context_word, mutual_count in suffix_co_occurence_dict[suffix].iteritems():
				try :
					dict_pmi[suffix][context_word] = max(math.log((float(mutual_count*total_word_count))/ind_count*context_word_count[context_word], 2), 0)
				except Error as e :
					print "context_word error:",context_word
                                        log_file.write("{},{}+\n".format(e,context_word))
		except KeyError as e :
			log_file.write(suffix+"\n")

		if count%10 ==0 :
			print count,"suffix"
	print "pmi done for suffixes"

	"""for derived_word,ind_count in derived_word_count.iteritems():
		for context_word, mutual_count in derived_co_occurence_dict[derived_word].iteritems():
			dict_pmi[derived_word][context_word] = max(math.log((float(mutual_count*total_word_count))/ind_count*context_word_count[context_word], 2), 0)
			
	for source_word,ind_count in source_word_count.iteritems():
        	for context_word, mutual_count in source_co_occurence_dict[source_word].iteritems():
            		dict_pmi[source_word][context_word] = max(math.log((float(mutual_count*total_word_count))/ind_count*context_word_count[context_word], 2), 0)	
	
	"""
	with open("pmi_values.json","wb+") as f:
		json.dump(dict_pmi,f)

	
if __name__ == "__main__" : 
	
	cal_pmi("/home/du3/13CS30045/lazaridou/")

	
