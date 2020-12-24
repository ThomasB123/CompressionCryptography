
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
#inputSize = os.path.getsize(inFile)
#print("Input file: \t" + inFile)
#print("Input size: \t" + str(inputSize) + "\n")

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

# LZW implementation:

inputFile = open(inFile,'r')
outputFile = open(encodedFile,'w')

characterStream = []
for line in inputFile:
    for character in line:
        characterStream.append(character)

def LZW():
    dictionary = {}
    for x in range(0,256):
        dictionary[chr(x)] = x
    i = 256
    characterIndex = 0
    string = ''
    while characterIndex < len(characterStream):
        string += characterStream[characterIndex]
        while (string in dictionary) and (characterIndex < len(characterStream)-1):
            characterIndex += 1
            string += characterStream[characterIndex]
        if string[:-1] not in dictionary:
            dictionary[string[:-1]] = i
            i += 1
        dictionary[string] = i
        i += 1
        outputFile.write(str(dictionary[string[:-1]])+',')
        string = string[-1]
        characterIndex += 1
    outputFile.write(str(dictionary[string[-1]]))
    # come back to this later:
    # think is related to character formattting or something

def updateModel(characterStream,context,maxOrder):
    index = 0
    while index < len(characterStream):
        currentCharacter = characterStream[index]
        for i in range(0,maxOrder+1):
            if index >= i:
                characters = ''.join(characterStream[index-i:index])
                if characters in context[i]:
                    if currentCharacter not in context[i][characters]:
                        context[i][characters][currentCharacter] = 1
                    else:
                        context[i][characters][currentCharacter] += 1
                else:
                    context[i][characters] = {None:1,currentCharacter:1} # Method A, None is escape character
        index += 1
    return context

def L(char,probs):
    low = 0
    if char == None:
        return 1-probs[None]
    for i in probs:
        if i != None:
            if i == char:
                return low
            low += probs[i]

def H(char,probs):
    high = 0
    if char == None:
        return 1
    for i in probs:
        if i != None:
            high += probs[i]
            if i == char:
                return high

def PPM(characterStream,context,maxOrder):
    #maxOrder = 2
    #context = {}
    #for i in range(maxOrder+1):
    #    context[i] = {}
    index = 0
    Low = 0
    Lstar = '000000'
    High = 63
    Hstar = '111111'
    while index < len(characterStream):
        #context = updateModel(characterStream[:index+1],context,maxOrder)
        currentCharacter = characterStream[index]
        # arithmetic coding here, but for each context
        contextOrder = maxOrder
        noContext = True
        while noContext: # reduce order of context if can't find
            if index >= contextOrder:
                characters = ''.join(characterStream[index-contextOrder:index])
                thisContext = context[contextOrder][characters] # should always be there if seen before
                total = 0
                # how do you work out how many bits for Low and High
                # assume 6 bit word length for arithmetic coding
                for x in thisContext:
                    total += thisContext[x]
                if currentCharacter in thisContext:
                    noContext = False
                    newLow = Low + (High-Low+1) * thisContext[currentCharacter]/total
                    newHigh = High + (High-Low+1) * thisContext[currentCharacter]/total - 1
                else:
                    newLow = Low + (High-Low+1) * thisContext[None]/total
                    newHigh = High + (High-Low+1) * thisContext[None]/total - 1
                Lstar = bin(int(newLow))[2:] # because 6 bit
                for i in range(6-len(Lstar)):
                    Lstar = '0' + Lstar
                Hstar = bin(int(newHigh))[2:] # because 6 bit
                for i in range(6-len(Hstar)):
                    Hstar = '0' + Hstar
                Low = newLow
                High = newHigh
                print(currentCharacter,Lstar,Hstar)
            contextOrder -= 1
        index += 1

# context based compression here:
# adaptive context
# use 5 character context for now
maxOrder = 2
context = {}
for i in range(maxOrder+1):
    context[i] = {}
newContext = updateModel(characterStream,context,maxOrder) # use this to update statistical model of text
print(newContext)
PPM(characterStream,newContext,2)
print(bin(int(1/3*64)))

inputFile.close()
outputFile.close()




########################################

# Runs your encoder and prints out size of encoded file
#encodedSize = os.path.getsize(encodedFile)
#print("Encoded file: \t" + encodedFile)
#print("Encoded size: \t" + str(encodedSize) + "\n")
#print("COMPRESSION RATIO: \t"  + str(inputSize / encodedSize)) # higher is better
