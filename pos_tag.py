# File tags the words of the Corpus, with their Parts of Speech 
# Input is the corpus. It also removes the stop words while tagging. 
# Output is a dictionary with fields : word,tags,frequency

import nltk 
import time 
from nltk.tag.perceptron import PerceptronTagger
import re
import json 
import cPickle as cp 
def clean_para(parag,stop_set):
        clean_parag = re.sub("[^a-zA-Z]"," ",parag)
        clean_parag = re.sub(" +"," ",clean_parag)
        clean_parag = re.sub("\n","",clean_parag)
        clean_parag=clean_parag.lower()
        clean_parag=' '.join( [w for w in clean_parag.split() if len(w)>1] )
        #stop_word = set(stopwords.words('english'))
	
	#f = open("stop_words.txt","rb+")

        
        word_set = [word for word in clean_parag.split(" ")]

        intersection = [word for word in word_set if word not in stop_set]
        clean_parag = " ".join(w for w in intersection)
        #f.close()
        return clean_parag

        

def get_tags() :
        n_lines =37609772
        corpus = open("/home/du3/13CS30045/datasets/enwiki/enwiki_merged.txt","r")
        count = 0
        print "Loaded Corpus" 
	# Removing the stop words
	f = open("stop_words.txt","rb+")
	stop_set = [re.sub("\n","",line) for line in f]	
	
	def update_list(temp_list,item):
		temp_list[0].append(item[1])
		temp_list[1]+=1
		return temp_list
	
	# Intialising the POS Tagger 
	tagger = PerceptronTagger()
	tagset = None 
	start = time.time()
	with open("pos_tag_dictionary2.json","a") as out_file:
        	for line in corpus :
			temp_dict = {}
			line = clean_para(line,stop_set)
			token_text = nltk.word_tokenize(line)
               		#print time.time()-start
			pos_list = nltk.tag._pos_tag(token_text,tagset,tagger)
			#print time.time()-start	
			count+=1
			if pos_list == [] :
				continue
			#print pos_list
			#temp_dict = {item[0]:[list(),0]  for item in pos_list}
			#temp_dict = {item[0]:update_list(temp_dict[item[0]],item) for item in pos_list if item[0] in temp_dict}
			#word_dict.update(temp_dict)
			for item in pos_list:
				temp_dict["word"] = item[0]
				temp_dict ["tag"] = item[1]
				temp_dict["count"] = 1
				json.dump(temp_dict,out_file)
			if count%100 == 0:
				print count,n_lines
			
			#print time.time()-start
			#print temp_dict
	f.close()
	#print "Dumping to json"		
	#with open("pos_tag_dictionary_1.json","wb+") as out_file:

		#json.dump(word_dict,out_file)
					
if __name__ == "__main__" :

        get_tags()

