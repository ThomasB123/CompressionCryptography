
import os
import sys
import struct

inFile = sys.argv[1]
fileName = inFile.split('.')[0]
encodedFile = fileName + '.lz'

# LZW:

n = os.path.getsize(inFile) # work out number of bits in file
maxTableSize = pow(2,int(n)) # define maximum table size
file = open(inFile, 'r', newline='')
data = file.read()

dictSize = 256
dictionary = {}
for i in range(dictSize):
    dictionary[chr(i)] = i

string = ''
tokens = []
for symbol in data:
    newString = string + symbol
    if newString in dictionary: # if already seen this sequence
        string = newString # extend
    else: # if this is a new sequence, then add it to dictionary
        tokens.append(dictionary[string])
        if len(dictionary) <= maxTableSize:
            dictionary[newString] = dictSize
            dictSize += 1
        string = symbol

if string in dictionary: # for last sequence at end of file
    tokens.append(dictionary[string])

# write tokens to file
outFile = open(encodedFile, 'wb')
if dictSize > 65535:
    mode = '>L' # 4 bytes per token (long), supports worst case scenario for files up to 4GB
    outFile.write(struct.pack('>B',1)) # write 1 if using long
else:
    mode = '>H' # 2 bytes per token (short), supports worst case scenario for files up to 65KB
    outFile.write(struct.pack('>B',0)) # write 0 if using short

for token in tokens:
    outFile.write(struct.pack(mode,int(token))) # unsigned integer, big-endian byte order

outFile.close()
file.close()



########################################

# statistical compression - two properties: frequency of symbols and context
# context-based compression
#   adaptive context, no more than 10 character context
#   prediction by partial matching PPM #####
#       Roshal Archive file format (RAR)
#   methods B and C
#   context mixing - PAQ series of programs ##########
#   Burrows-Wheeler Transform (BWT) #####

########################################


# other attempts:

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
