
import sys
import struct

inFile = sys.argv[1]
fileName = inFile.split('.')[0]
decodedFile = fileName + '-decoded.tex'

# LZW:

file = open(inFile, 'rb')
tokens = []
nextCode = 256
plaintext = ''
string = ''

(byteType, ) = struct.unpack('>B',file.read(1)) # read 1st byte of file, which is a 0 or 1
if byteType == 4: # if 4 then each token is 4 bytes, long unsigned integer
    while True:
        token = file.read(4) # read x bytes at a time to get each token
        if len(token) != 4:
            break
        (data, ) = struct.unpack('>L', token) # unsigned long integer and big-endian byte order
        tokens.append(data)
elif byteType == 3: # if 3 then each token is 3 bytes
    while True:
        token = file.read(3) # read x bytes at a time to get each token
        if len(token) != 3:
            break
        (data, ) = struct.unpack('>L', b'\0' + token) # unsigned integer and big-endian byte order
        tokens.append(data)
else: # if 2 then each token is 2 bytes, short unsigned integer
    while True:
        token = file.read(2) # read x bytes at a time to get each token
        if len(token) != 2:
            break
        (data, ) = struct.unpack('>H', token) # unsigned integer and big-endian byte order
        tokens.append(data)

# Building and initializing the dictionary
dictSize = 256
dictionary = {}
for i in range(dictSize):
    dictionary[i] = chr(i)

# iterating through the codes.
# LZW Decompression algorithm
for code in tokens:
    if code not in dictionary:
        dictionary[code] = string + string[0]
    plaintext += dictionary[code]
    if len(string) != 0:
        dictionary[nextCode] = string + dictionary[code][0]
        nextCode += 1
    string = dictionary[code]

# storing the decompressed string into a file
outFile = open(decodedFile, 'w', newline='')
for data in plaintext:
    outFile.write(data)
    
outFile.close()
file.close()

