# up to 6 ideas explained in the report (5 marks each), format same as Max's lecture notes.
# Can implement more than 6 ideas as long as different.
# he is using just zip file, gives 30% file size increase, to check for not-trivial answers, would get 2 marks for that.
# can't have all 6 ideas from lecture notes, because would be redundant
# should have some original ideas, from looking elsewhere and thinking of other things yourself
# file will be roughly 1 MB, can take 10 or 20 minutes if neccessary and he's fine with that
# if program works on this script then it should work
# code doesn't need to be commented, is good practice for yourself but he doesn't require it

# Test your encoder and decoder with input file specified by the user

# Usage: python testEncoderDecoder.py testFile
# where testFile.tex is the name of the input tex file

import os
import sys

testFile        = sys.argv[1]
inputFile       = testFile + ".tex"
encodedFile     = testFile + ".lz"
decodedFile     = testFile + "-decoded.tex"


# Size of input file
inputSize = os.path.getsize(inputFile)
print("Input file: \t" + inputFile)
print("Input size: \t" + str(inputSize) + "\n")

# Runs your encoder and prints out size of encoded file
os.system("python3 encoder.py " + inputFile)
encodedSize = os.path.getsize(encodedFile)
print("Encoded file: \t" + encodedFile)
print("Encoded size: \t" + str(encodedSize) + "\n")


# Runs your decoder and prints out size of decoded file
os.system("python3 decoder.py " + encodedFile)
decodedSize = os.path.getsize(decodedFile)
print("Decoded file: \t" + decodedFile)
print("Decoded size: \t"  + str(decodedSize) + "\n")

# Checks whether input and decoded files have the same size
if decodedSize != inputSize:
    print("ERROR: Incorrect decoded file size")
else:
    # Checks that input and decoded files are the same
    if open(inputFile,'r').read() != open(decodedFile,'r').read():
        print("\n ERROR: Incorrect decoded file contents")
    else:
        # Files are the same.
        print("\nSUCCESS: Lossless compression" )
        print("COMPRESSION RATIO: \t"  + str(inputSize / encodedSize))
