# Cleans the corpus to remove stop words, 
# Input : enwiki_merged.txt
# Output : enwiki_cleaned.txt
import nltk
import re
def clean_para(parag):
        clean_parag = re.sub("[^a-zA-Z]"," ",parag)
        clean_parag = re.sub(" +"," ",clean_parag)
        clean_parag = re.sub("\n","",clean_parag)
        clean_parag=clean_parag.lower()

	f = open("stop_words.txt","rb+")
        clean_parag=' '.join([w for w in clean_parag.split() if len(w)>1])

	stop_set = [re.sub("\n","",line) for line in f]

	
	word_set = [word for word in clean_parag.split(" ")]
		
	intersection = [word for word in word_set if word not in stop_set]
	clean_parag = " ".join(w for w in intersection)
	f.close()
	return clean_parag

def clean_corpus() :
	n_lines = 48071436
	corpus = open("/home/du3/13CS30045/datasets/enwiki/enwiki_merged.txt","r")
	count = 0  
	with open("/home/du3/13CS30045/datasets/enwiki/enwiki_cleaned.txt","wb+") as input_file:

		for line in corpus :
			count+=1
			if count%100 == 0 :
				print count,n_lines				
		 	if line.strip() == "" :
				continue			
			line1 = clean_para(line)
			input_file.write(line1+"\n")


if __name__ == "__main__" :

	clean_corpus()
	#clean_para("It seems an oracular cult existed in Delphi from the Mycenaean ages. In historical times, the priests of Delphi were called Labryaden, which indicates Minoan origin. The double-axe, labrys, was the holy symbol of the Cretan labyrinth. The Homeric hymn adds that Apollo appeared as a dolphin and carried Cretan priests to Delphi, where they evidently transferred their religious practices.  was a sea-god especially worshiped in Crete and in the islands, and his name indicates his connection with Delphi and the holy serpent Delphyne . Apollo's sister Artemis, who was the Greek goddess of hunting, is identified with Britomartis (Diktynna), the Minoan . In her earliest depictions she is accompanied by the, a male god of hunting who had the bow as his attribute. His original name is unknown, but it seems that he was absorbed by the more popular Apollo, who stood by the virgin , becoming her broth ")
