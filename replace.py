import csv
import fileinput
def sdw_list(csv_file):

	derived_word_dict = {}
	with open(csv_file, 'rb') as f:
		#reader = csv.reader(f)
		#my_list = list(reader)
		for line in f :
			line_word = line.split(",")
			derived_word_dict[line_word[3]] = [line_word[1],line_word[0]]
	return derived_word_dict

def replace_corpus(path_to_files):
		
	derived_word_dict = sdw_list("/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files/source_derived_words_stats.csv")
		

	out_file = open("replaced_corpus.txt", 'wb+')
		
	with open(path_to_files+"enwiki_cleaned.txt",'rb+') as en:
                count = 0
                for line in en:
                        count += 1
                        for word in line.split():
                                if word in derived_word_dict:
					
					out_file.write(derived_word_dict[word][0]+" "+derived_word_dict[word][1]+" ")

                                else:   
                                        out_file.write(word + " ")
                        if count %1000 == 0:
                                print count, "/37609772"
                        out_file.write("\n")



if __name__ == "__main__":
	

	replace_corpus("/home/du3/13CS30045/affix_final/datasets/enwiki/")





	"""derived_list = sdw_list("/home/du3/13CS30045/affix_final/lazaridou/create_vectors/data_files/source_derived_words_stats.csv")
	create_dset = []
	for i in range(len(derived_list)):
		create_dset.append(derived_list[i][3])
	derived_set = set(create_dset)
	out = open("replaced_corpus.txt", 'w+')
	with open("enwiki_cleaned.txt", 'r') as en:
		count = 0
		for line in en:
			count += 1
			for word in line.split():
				if word in derived_set:
					for x_list in derived_list:
						if word == x_list[3]:
							out.write(x_list[1]+" "+x_list[0]+" ")
		

				else:
					out.write(word + " ")
			if count %1000 == 0:
				print count, "/37609772"
			out.write("\n")

	out.close()"""
