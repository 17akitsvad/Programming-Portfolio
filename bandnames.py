#Band name generator
import random
titles = ["gigantic", "sour", "steamy", "gross", "stupid", "ironic", "greasy", 
			"tangy", "smelly", "small", "inventive", "spherical", "spiritual", "green",
			"blue", "pot bellied", "pickled", "prickly"]

adjs = ['tiny', 'fat', 'shiny', 'ecclectic', 'fluffy' , 'bright', 'corrrupt', 
		'aggressive', 'alarming', 'amazing', 'magical', 'courageous', 'fierce', 
		'colorless', 'red', 'thoughtless', 'smart', 'delirious', 'fabulous',
		'fergalicious', 'dangerous']

plural_nouns = ['apples', 'oranges', 'kiwis', 'clementines', 'wildabeasts',
				'mammoths', 'rabbits', 'sloths', 'crashes', 'spices', 'eggs', 'herbs',
				'pony tails', 'bears', 'snitches', 'unicorns', 'kermits', 'signs', 
				'indians', 'cowboys']

def title():
	'''This function chooses a random title for the name '''
	return random.choice(titles).capitalize()
def adj():
	''' This function chooses a random adj for the band '''
	return random.choice(adjs).capitalize()
def plural_noun():
	return random.choice(plural_nouns).capitalize()
def main():
	while True:
		name = raw_input("Enter your name:")
		if name == "q":
			break
		random.seed(name)
		print title(), name, " And The ", adj(), plural_noun()
		
main()