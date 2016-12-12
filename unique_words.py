# File counts the unique words in the corpus 
import nltk 
import re 
def clean_parag(parag):
        clean_parag = re.sub("[^a-zA-Z]"," ",parag)
        clean_parag = re.sub(" +"," ",clean_parag)
        clean_parag = re.sub("\n","",clean_parag)
        clean_parag=clean_parag.lower()
        clean_parag=' '.join( [w for w in clean_parag.split() if len(w)>1] )
        return clean_parag


def count_words():
	n_lines =48071436
	count =0 
	word_list = set()
	with open("/home/du3/13CS30045/datasets/enwiki/enwiki_merged.txt","r") as f:
		for line in f :
			count+=1
			#line = clean_parag(line)
			print count,n_lines
			for word in line.split(" "):	
				word_list.add(word)
	print len(word_list)
	unique_words = 4542741
if __name__ == "__main__":
	count_words()
