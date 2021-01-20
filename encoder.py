
import os
import sys
import zipfile

inFile = sys.argv[1]
fileName = inFile.split('.')[0]
encodedFile = fileName + '.lz'

# I am just using zip because none of implementations work
zipfile.ZipFile(encodedFile, 'w').write(inFile)

########################################

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

# Plan:
# Huffman
# Context Mixing
# LZW
# BWT
# Move-To-Front
# Run-Length-Encoding

# remember to accommodate both \n and \n\r

########################################


# attempts:


# LZW implementation:
'''
inputFile = open(inFile,'rb')
outputFile = open(encodedFile,'wb')

data = inputFile.read()
characterStream = []
for byte in data:
    characterStream.append(bytes([byte]))

def LZW():
    dictionary = {}
    for x in range(0,256):
        dictionary[bytes(chr(x),'utf-8')] = x
    i = 256
    characterIndex = 0
    #string = b''
    while characterIndex < len(characterStream):
        try:
            string += bytes([characterStream[characterIndex]])
        except:
            string = characterStream[characterIndex]
        while (string in dictionary) and (characterIndex < len(characterStream)-1):
            characterIndex += 1
            string += characterStream[characterIndex]
        if string[:-1] not in dictionary:
            dictionary[string[:-1]] = i
            i += 1
        dictionary[string] = i
        i += 1
        #print(dictionary[string[:-1]].to_bytes(2,byteorder='big'))
        outputFile.write(dictionary[string[:-1]].to_bytes(2,byteorder='big'))
        string = string[-1]
        characterIndex += 1
    outputFile.write(string.to_bytes(2,byteorder='big'))
    # come back to this later:
    # think is related to character formattting or something

LZW()
'''

# PPM implementation:
'''
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

# use 5 character context for now

maxOrder = 5
context = {}
for i in range(maxOrder+1):
    context[i] = {}
newContext = updateModel(characterStream,context,maxOrder) # use this to update statistical model of text
print(newContext)
PPM(characterStream,newContext,2)
print(bin(int(1/3*64)))
'''
