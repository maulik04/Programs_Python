#!/usr/bin/python -tt

####################### MAULIK BHENSDADIA #####################


def main():
	name = str(raw_input("Enter a word: ")); ## CLI INPUT 
	print len(name)
	vowels = 0 
	for character in name:    ## Match vowel character in INPUT
	    if character == 'a': 
	        vowels += 1 
	    if character == 'e': 
	        vowels += 1 
	    if character == 'i': 
	        vowels += 1 
	    if character == 'o': 
	        vowels += 1 
	    if character == 'u': 
	        vowels += 1
	print ("We found", vowels, "Number of vowels:")
	nonvowels = len(name) - vowels  ## find nonvowel numbers
	print ("We found", nonvowels, "Number of nonvowels:")

if __name__ == '__main__':
	main()

