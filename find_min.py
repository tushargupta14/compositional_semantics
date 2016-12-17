


def  find_min() : 

	f = open("context_word.csv","rb+")
	min = ["",10000]
	i =0
	print "here"
	for line in f:
		word = line.split(",")
		#print word 
		i+=1 
		print i  
		if int(word[1]) <= min[1] :
			min[1] = int(word[1])
			min[0] = word[0]
	print min

if __name__ == "__main__" :
	
	find_min()
