import sys

open_file = open(sys.argv[1])

def word_inventory(file):

	""" This function produces a list indexing the number of words by length
	>>> word_inventory("& I thought so too, that he wasn't @ home!")
	[2, 1, 2, 1, 2, 1, 0, 1]
	"""
	
	text = file.read()
	    
	textlst = []
	
	
	for punc in ",.?!:;'\"":
	    text = text.replace(punc, '')
	    textlst = text.split()
	
	greatest = 0
	
	for word in textlst:
	    if len(word) > greatest:
	        greatest = len(word)
	        
	lengthct = [0]*(greatest+1)
	
	symbols = "@&*#$"
	
	for word in textlst:
	    if word not in symbols:
	        lengthct[len(word)] += 1
	      
	return lengthct

    
lengthcount = word_inventory(open_file)
for ind, ct in enumerate(lengthcount):
    if ct:
        print("Length", ind, ":", ct)
    
    
for y in range(300,9,-10):	#decrease by 10 from 300 to 10
    print("{:<5} |".format(y), end="")	#indicate y axis number, but remain on x axis
    for x in range(1, len(lengthcount)):	#iterate through list of word frequencies by length, each length is a column
        if lengthcount[x] >= y:	#in case the word frequency meets condition (and the first time any frequency does, it always will for each value of y), indicate on x axis...
            column = "***"	#with three asterisks...
        else:
            column = "   "	#or with three spaces.
        print(column, end="") #output for each list index
    print()	#once inner loop ranges through x axis, move to next point along y axis, i.e. next row
print("      -",end="")	#white space to align beginning of x with the y axis, the dash ends 0 to let 1 decoration begin
for ct in lengthcount: # range through the index of word lengths
    if ct: #ensure decoration for each index starts at one
        print("-+-", end="")
print()
print("        ",end="")	#white space to align numbers with decoration
for ct in range(1, len(lengthcount)):	#range through word lengths, starting at one
    if ct <= 8:	#include necessary white space for single digit numbers
        print(ct," ",end="")
    if ct > 8:	#strip white space for double digit numbers
        print(ct,"",end="")
        


    