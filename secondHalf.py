
import os
import json
import subprocess
import time

with open('data4.json','r') as infile:
    data = json.load(infile)
print(len(data))

#array = []
#for i in data:
#    array.append(i)
#print(array[35093])
#print(array[6272674])
#exit()

start = time.time()
i = 0
toEncrypt = ''
reference = {}
encryptedData = {}
for x in data:
    toEncrypt += x
    reference[i] = x
    if i % 2047 == 0:
        encrypted = subprocess.run(['encrypt.exe',toEncrypt],stdout=subprocess.PIPE).stdout.decode('utf-8')[:-2]
        for y in range(len(encrypted)//16-1):
            encryptedData[encrypted[y*16:y*16+16]] = y
            if 'aeb47ca88390c475' in encryptedData:
                index = encryptedData['aeb47ca88390c475']
                #index = encryptedData['903408ec4d951acf']
                print(index+((i-1//2047)*2047+1))
                print(reference[index+((i-1//2047)*2047)+1])
                print('Found it!')
                end = time.time()
                print('Took',end-start,'seconds')
                exit()
            toEncrypt = ''
            print(i)
    i += 1

