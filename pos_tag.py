import nltk
import re
import json 
import cPickle as cp 
def clean_para(parag):
        clean_parag = re.sub("[^a-zA-Z]"," ",parag)
        clean_parag = re.sub(" +"," ",clean_parag)
        clean_parag = re.sub("\n","",clean_parag)
        clean_parag=clean_parag.lower()
        clean_parag=' '.join( [w for w in clean_parag.split() if len(w)>1] )
        #stop_word = set(stopwords.words('english'))
        return clean_parag

def get_tags() :
        n_lines =48071436
        corpus = open("/home/du3/13CS30045/datasets/enwiki/enwiki_merged.txt","r")
        count = 0
        word_list ={}
	
	
        for line in corpus :
		line = clean_para(line)
		#print "line",line 
		token_text = nltk.word_tokenize(line)
               	
		pos_list = nltk.pos_tag(token_text)
		#print "pos_list",pos_list
		count+=1
		if pos_list == [] :
			continue

		for item in pos_list :
			#print item 	
			if item[0] not in word_list :
				word_list[item[0]] = [list(),1]
				word_list[item[0]][0].append(item[1])
			elif item[0] in word_list :
				word_list[item[0]][0].append(item[1])
				word_list[item[0]][1]+=1
		#print word_list  
		
		if count%100==0:
			print count,n_lines
	with open("pos_tag_dictionary.json","wb+") as f:
		json.dump(word_list,f)
					
if __name__ == "__main__" :

        get_tags()

