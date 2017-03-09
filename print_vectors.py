#file loads a fastText model and prints word vectors for a set of affixes given in target_words.txt

import subprocess
import shlex


def print_vectors_fulladd(target_dir):
	
	input_file = target_dir+"source_words.txt"
        output_file = target_dir+"source_vectors.txt"

        command = "cat " + input_file +" | ./fasttext print-vectors /home/du3/13CS30045/affix_final/datasets/enwiki/fasText_results/model5.bin > "+output_file

        p = subprocess.Popen(command,cwd = "/home/du3/13CS30045/fastText",shell=True)
        #print "fastText running for",affix
        p.communicate()


        print "source fastText finished."

        input_file = target_dir+"derived_words.txt"
        output_file = target_dir+"derived_vectors.txt"

        command = "cat " + input_file +" | ./fasttext print-vectors /home/du3/13CS30045/affix_final/datasets/enwiki/fasText_results/model7.bin > "+output_file

        p = subprocess.Popen(command,cwd = "/home/du3/13CS30045/fastText",shell=True)
        #print "fastText running for",affix
        p.communicate()

        print "fastText for derived words finished"

	input_file = target_dir+"affix_words.txt"
        output_file = target_dir+"affix_vectors.txt"

        command = "cat " + input_file +" | ./fasttext print-vectors /home/du3/13CS30045/affix_final/datasets/enwiki/fasText_results/model7.bin > "+output_file

        p = subprocess.Popen(command,cwd = "/home/du3/13CS30045/fastText",shell=True)
        #print "fastText running for",affix
        p.communicate()
	
	

def print_vectors(path_to_files):
	
	#input_file=raw_input()
	#output_file=raw_input()
	
	#command = "cat /home/du3/13CS30045/tushar/target_words.txt | ./fasttext print-vectors /home/du3/13CS30045/datasets/enwiki/enwiki_model.bin > vectors.txt"
	input_file = path_to_files+"fastText_input.txt"
	output_file = path_to_files + "fastText_vectors.txt"
	
	command = "cat " + input_file +" | ./fasttext print-vectors /home/du3/13CS30045/affix_final/datasets/enwiki/fasText_results/model7.bin > "+output_file

	p = subprocess.Popen(command,cwd = "/home/du3/13CS30045/fastText",shell=True)	
	#print "fastText running for",affix
	p.communicate()

	
	print "fastText finished."

	"""input_file = target_dir + affix+"_derived_words.txt"
        output_file = target_dir+affix+"_derived_vectors.txt"
        
        command = "cat " + input_file +" | ./fasttext print-vectors /home/du3/13CS30045/affix_final/datasets/enwiki/fasText_results/model7.bin > "+output_file

        p = subprocess.Popen(command,cwd = "/home/du3/13CS30045/fastText",shell=True)   
        print "fastText running for",affix
        p.communicate()
	
	print "fastText for derived words finished"""



if __name__ == "__main__":

 	path_to_files = "/home/du3/13CS30045/affix_final/lazaridou/"	
	print_vectors(path_to_files)
