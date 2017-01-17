# word intersection takes the source words and the derived words and takes out the words present both in wiktionary and the wikipedia corpus 
# Output : source_list_with_counts.csv with source words appended with their counts 
# derived_list_with_counts.csv  derived words + counts appended  


import json 
from collections import defaultdict

def suffix_counts(path_to_files) :
	## Function calculates the count of a suffix with which its derived words are present 
	derived_file  = open(path_to_files+"derived_list_with_counts.csv","rb+")
	
	derived_dict = {}
	
	derived_dict  = { line.split(",")[0]:line.split(",")[1] for line in derived_file}
	w_c = 0
	#print derived_dict["venography"]
	with open(path_to_files+"suffix_derived_words.json","r") as f:
		suffix_dict = json.load(f)
	suffix_dict_with_counts = defaultdict(list)	
	for key,value in suffix_dict.iteritems():
		for word in value :
			if word in derived_dict:
				w_c+=1
				suffix_dict_with_counts[key].append((word,derived_dict[word].rstrip()))
	print len(suffix_dict_with_counts)			
	
	count = 0 
	#for key,value in suffix_dict_with_counts.iteritems():
		#print key,value 
		#count+=1
		#if count == 1:
			#break 			
	#print w_c 

	with open("suffix_dict_with_counts.json","wb+") as f:
		json.dump(suffix_dict_with_counts,f)
def word_intersection(path_to_files) :

	source_file = open(path_to_files+"source_words.csv", "rb+")
	derived_file  = open(path_to_files+"derived_words.csv","rb+")
		
	source_set = set()
	derived_set = set()
	for line in source_file :
		source_set.add(line.rstrip())
	print "source words",len(source_set)
	for line in derived_file:
		derived_set.add(line.rstrip())
	print "derived words",len(derived_set)
	#print source_set 
	common_source_word_list = []
	common_derived_word_list = []
	count = 0

	with open(path_to_files+"word_count.csv","rb+") as f:
		for line in f :
			count+=1
			word = line.split(",")
			#print word			
			if word[0] in source_set :
				common_source_word_list.append((word[0],int(word[1])))
			elif word[0] in derived_set :
				common_derived_word_list.append((word[0],int(word[1])))
			print count 
 	print len(common_source_word_list),len(common_derived_word_list) 
	#print common_derived_word_list,common_source_word_list
	
	fp1 = open("source_list_with_counts.csv","a")
	for item in common_source_word_list :
		fp1.write(item[0]+","+str(item[1])+"\n")
	fp2 = open("derived_list_with_counts.csv","a")
	for item in common_derived_word_list :
		fp2.write(item[0]+","+str(item[1])+"\n")
	fp1.close()
	fp2.close()
if __name__ == "__main__" :

	word_intersection("/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files/")	
