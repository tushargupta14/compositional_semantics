import nltk
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
        n_lines =48071436
        corpus = open("/home/du3/13CS30045/datasets/enwiki/enwiki_merged.txt","r")
        count = 0
        word_dict ={}
	f = open("stop_words.txt","rb+")
	stop_set = [re.sub("\n","",line) for line in f]	
	def update_list(temp_list,item):
		temp_list[0].append(item[1])
		temp_list[1]+=1
		return temp_list
	
        for line in corpus :
		line = clean_para(line,stop_set)
		token_text = nltk.word_tokenize(line)
               	
		pos_list = nltk.pos_tag(token_text)
	
		count+=1
		if pos_list == [] :
			continue
		
		temp_dict = {item[0]:[list(),0]  for item in pos_list}
		temp_dict = {item[0]:update_list(temp_dict[item[0]],item) for item in pos_list if item[0] in temp_dict}
		word_dict.update(temp_dict)
	
		if count%100==0:
			print count,n_lines
	#print word_dict
	f.close()
	print "Dumping to json"		
	with open("pos_tag_dictionary_1.json","wb+") as out_file:

		json.dump(word_dict,out_file)
					
if __name__ == "__main__" :

        get_tags()

