
import os
import sys
import zipfile
import tempfile

inFile = sys.argv[1]
fileName = inFile.split('.')[0]
decodedFile = fileName + '-decoded.tex'

# I am just using zip because none of implementations work
with tempfile.TemporaryDirectory() as tmpDir: # create temporary folder for extraction
    zipfile.ZipFile(inFile, 'r').extractall(tmpDir) # extract .tex file to temporary folder
    os.rename(tmpDir + '/' + fileName + '.tex', decodedFile) # move decoded file out of temporary folder


# attempt at decoding LZW:
'''
inputFile = open(inFile,'rb')
outputFile = open(decodedFile,'w')

data = inputFile.read()
characterStream = []
for i in range(0,len(data),2):
    characterStream.append(str(data[i]+data[i+1]))

dictionary = []
for x in range(0,256):
    dictionary.append(chr(x))
i = 256
characterIndex = 0
current = ''
while characterIndex < len(characterStream):
    number = int(characterStream[characterIndex])
    if number < len(dictionary):
        for x in dictionary[number]:
            current += x
            if current not in dictionary:
                dictionary.append(current)
                current = current[-1]
        outputFile.write(dictionary[number])
    else:
        pass
        #dictionary.append()
    characterIndex += 1

inputFile.close()
outputFile.close()
'''
