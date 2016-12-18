#Output :  Creates the files to be input to dissect library : corpus.rows, corpus.cols, corpus.sm 


import json 

def create_rows_file(path_to_files):

	source_file = open(path_to_files+"source_list_with_counts.csv","rb+")	
 	derived_file = open(path_to_files+"derived_list_with_counts.csv","rb+")
		
	with open("suffix_dict_with_counts.json","rb+") as fp :
		suffix_dict = json.load(fp)
	outfile = open(path_to_files+"corpus.rows","wb+")
	for line in source_file :
		outfile.write(line.split(",")[0]+"\n")
	for line in derived_file :
                outfile.write(line.split(",")[0]+"\n")
 	for key in suffix_dict.iterkeys() :
		outfile.write(key+"\n")
	outfile.close()
	derived_file.close()
	source_file.close()
		


def create_cols_file(path_to_files):
	
	context_file = open(path_to_files+"context_word.csv","rb+")
	outfile = open(path_to_files+"corpus.cols","wb+")
        for line in context_file :
                outfile.write(line.split(",")[0]+"\n")
	
	outfile.close()
	context_file.close()

def co_occurence_file(path_to_files): 

# source_co_occurence_matrix.json, derived_co_occurence_matrix.json, suffix_co_occurence_matrix.json

# Output file : co_occurence_matrix.sm 
	in_file = open(path_to_files+"source_co_occurence_matrix.json")	



if __name__ == "__main__" :

	create_rows_file("/home/du3/13CS30045/lazaridou/")
	#create_cols_file("/home/du3/13CS30045/lazaridou/")
