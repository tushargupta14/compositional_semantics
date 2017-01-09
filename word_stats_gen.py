import sys 
import os 
# Script finds the set of instances where source words are present in the corpus and derived words are not and vice versa.
# Input : Path to the suffix files in the wiktionary folder 
# Final output : source_derived_word_stats.csv with the occurence values 


def generate_stats(path_to_affix_files):

	path_to_word_files = "/home/du3/13CS30045/affix_final/lazaridou/"
	word_count_dict = {}

	with  open(path_to_word_files+"word_count.csv","rb+") as f :
		word_count_dict = { line.split(",")[0]:int(line.split(",")[1].rstrip()) for line in f}
	
	print word_count_dict["shabag"]	

	files = os.listdir(path_to_affix_files)	
	count =0 
	out_file = open("source_derived_words_stats.csv","wb+")
	out_file.write("Affix,Source Word,Source Word Count,Derived Word,Derived word count\n")
	for affix_file in files :
		
		print affix_file	
		suffix = affix_file[1:]

		with open(path_to_affix_files+affix_file) as fp :
			for line in fp:
				s_word_count =0	
				d_word_count = 0
               			count += 1
               			row = line.split(',')
				if len(row) < 4:
                    			#corrupt += 1
                    			continue
				source_word = row[2]
				derived_word = row[1]
				if source_word in word_count_dict and derived_word in word_count_dict:
					s_word_count = word_count_dict[source_word]
					d_word_count = word_count_dict[derived_word]
				
				
				out_file.write("{},{},{},{},{}\n".format(suffix,source_word,s_word_count,derived_word,d_word_count))
				if  count%100 == 0:
					print count  
			

	






if __name__ == "__main__" : 

	generate_stats("/home/du3/13CS30045/affix_final/wiktionary/results_dec_2/")	
