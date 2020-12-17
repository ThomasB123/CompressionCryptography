
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



with open(encodedFile,'w') as fout:
    fin = open(inFile,'r')
    for line in fin:
        fout.write(line)




########################################

# Runs your encoder and prints out size of encoded file
encodedSize = os.path.getsize(encodedFile)
print("Encoded file: \t" + encodedFile)
print("Encoded size: \t" + str(encodedSize) + "\n")

