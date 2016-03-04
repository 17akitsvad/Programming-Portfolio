def ana(beg, end):
	
	
	
	
def anagrams(letters):
	dictionary = []
	try:
		dictionary_file = open("american-english.txt", "rb")
	except:
		print"Dictionary file not found"
		dictionary = None
		
	for line in dictionary_file:
		dictionary.append(line.strip())
	
	real_words = []
	words = ana("", letters)
	print"number of anagrams: ", len(words)
	
	
	for word in words:
		if len(word) > 1 and 