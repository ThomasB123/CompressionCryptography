
import os
import sys


if len(sys.argv) == 1:
    inFile = input('Enter a .lz file name > ')
elif len(sys.argv) > 2:
    print('You must only give 1 file name')
    exit()
else:
    inFile = sys.argv[1]
if '.' not in inFile:
    print('Please give a valid file name')
    exit()
if inFile.split('.')[1] != 'lz':
    print('You must give a .lz file')
    exit()
if not os.path.isfile(inFile):
    print('That is not a valid file name')
    exit()
fileName = inFile.split('.')[0]
decodedFile = fileName + '-decoded.tex'


# Size of input file
inputSize = os.path.getsize(inFile)
print("Input file: \t" + inFile)
print("Input size: \t" + str(inputSize) + "\n")

########################################
# do decoding here


inputFile = open(inFile,'r')
outputFile = open(encodedFile,'a')
characterStream = []
for line in inputFile:
    for character in line:
        characterStream.append(character)

i = 0
while i < len(characterStream):
    
    i += 1



########################################

# Runs your decoder and prints out size of decoded file
decodedSize = os.path.getsize(decodedFile)
print("Decoded file: \t" + decodedFile)
print("Decoded size: \t"  + str(decodedSize) + "\n")
