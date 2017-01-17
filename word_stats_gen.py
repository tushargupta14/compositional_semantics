import sys 
import os 
# Script finds the set of instances where source words are present in the corpus and derived words are not and vice versa.
# Input : Path to the suffix files in the wiktionary folder 
# Final output : source_derived_word_stats.csv with the occurence values 


def generate_stats(path_to_affix_files):

	path_to_word_files = "/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files"
	word_count_dict = {}

	with  open(path_to_word_files+"word_count.csv","rb+") as f :   ## word_count
		word_count_dict = { line.split(",")[0]:int(line.split(",")[1].rstrip()) for line in f}
	
	#print word_count_dict["shabag"]	

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
			

def generate_non_zero_word_stats(path_to_affix_files):

## Function only generates stats for word which appear in the corpus non-zero times
	path_to_word_files = "/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files/"
        word_count_dict = {}

        with  open(path_to_word_files+"word_count.csv","rb+") as f :   ## word_count
                word_count_dict = { line.split(",")[0]:int(line.split(",")[1].rstrip()) for line in f}

        #print word_count_dict["shabag"]        

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
				if s_word_count is not 0 or d_word_count is not 0 :

                                	out_file.write("{},{},{},{},{}\n".format(suffix,source_word,s_word_count,derived_word,d_word_count))
                                if  count%100 == 0:
                                        print count


	
	

	

	
"""
def generate_stats_for_able(path_to_json_file,path_to_csv_files):

	# able_word_stats file to have word and its count generated for able 
	suffix = "able"
	word_count_dict = {}
	with  open(path_to_csv_files+"able_word_stats.csv","rb+") as f :
                word_count_dict = { line.split(",")[0]:int(line.split(",")[1].rstrip()) for line in f}
	
	data_file = open(path_to_json_file+"able_minimal.json")
	out_file = open("source_derived_words_stats_able.csv","wb+")
	for row in data_file :
		s_word_count = 0
		d_word_count = 0
		j_object = json.loads(row)
		source_word = j_object["source_word"]
		derived_word = j_object["derived_word"]
		
		if source_word in word_count_dict and derived_word in word_count_dict:
			s_word_count = word_count_dict[source_word]
                        d_word_count = word_count_dict[derived_word]
		out_file.write("{},{},{},{}\n".format(suffix,source_word,s_word_count,derived_word,d_word_count))
	
	out_file.close()
	data_file.close()
"""
def generate_stats_for_able(path_to_affix_files):

	path_to_word_files = "/home/du3/13CS30045/affix_final/lazaridou/"
        word_count_dict = {}

        with  open(path_to_word_files+"able_count.csv","rb+") as f :   ## word_count
                word_count_dict = { line.split(",")[0]:int(line.split(",")[1].rstrip()) for line in f}

	count =0
        out_file = open("able_source_derived_words_stats.csv","wb+")
        out_file.write("Affix,Source Word,Source Word Count,Derived Word,Derived word count\n")
	
	affix_file = "-able"
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

	generate_non_zero_word_stats("/home/du3/13CS30045/affix_final/wiktionary/results_dec_2/")	
