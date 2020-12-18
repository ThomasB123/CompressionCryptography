
# up to 6 ideas explained in the report (5 marks each), format same as Max's lecture notes.
# Can implement more than 6 ideas as long as different.
# he is using just zip file, gives 30% file size increase, to check for not-trivial answers, would get 2 marks for that.
# can't have all 6 ideas from lecture notes, because would be redundant
# should have some original ideas, from looking elsewhere and thinking of other things yourself
# file will be roughly 1 MB, can take 10 or 20 minutes if neccessary and he's fine with that
# if program works on this script then it should work
# code doesn't need to be commented, is good practice for yourself but he doesn't require it


import os
import sys

if len(sys.argv) == 1:
    inFile = input('Enter a .tex file name > ')
elif len(sys.argv) > 2:
    print('You must only give 1 file name')
    exit()
else:
    inFile = sys.argv[1]
if '.' not in inFile:
    print('Please give a valid file name')
    exit()
if inFile.split('.')[1] != 'tex':
    print('You must give a .tex file')
    exit()
if not os.path.isfile(inFile):
    print('That is not a valid file name')
    exit()
fileName = inFile.split('.')[0]
encodedFile = fileName + '.lz'


# Size of input file
inputSize = os.path.getsize(inFile)
print("Input file: \t" + inFile)
print("Input size: \t" + str(inputSize) + "\n")

########################################
# do encoding here
# zip command line gets 2.5-3 compression ratio

# ideas:
# read lecture 35 and 36
# statistical compression - two properties: frequency of symbols and context
#   Huffman coding
#       prefix codes
#       use canonical huffman tree
#       adaptive huffman coding
#       codewords are only defined for symbols not messsages
#   Arithmetic coding
#       works at the sequence level, assigning a particular tag to any sequence,
#       without working out all tags for all sequences of the same length
#       better than huffman 
#       use integers only in practice
#       carry out operations in binary not decimal
# structural compression
#   Lempel-Ziv LZ77
#       two methods above are for memoryless source
#       this is for encoding fixed file of data efficiently
#   Lempel-Ziv LZ78
#       LZW
#       LZMW, LZAP, LZY ####################
# context-based compression
#   adaptive context, no more than 10 character context
#   prediction by partial matching PPM #####
#       Roshal Archive file format (RAR)
#   methods B and C
#   context mixing - PAQ series of programs ##########
#   Burrows-Wheeler Transform (BWT) #####

# huffman coding and then run length encoding?

with open(encodedFile,'w') as fout:
    fin = open(inFile,'r')
    for line in fin:
        fout.write(line)





########################################

# Runs your encoder and prints out size of encoded file
encodedSize = os.path.getsize(encodedFile)
print("Encoded file: \t" + encodedFile)
print("Encoded size: \t" + str(encodedSize) + "\n")
print("COMPRESSION RATIO: \t"  + str(inputSize / encodedSize)) # higher is better
