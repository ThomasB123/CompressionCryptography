
import os
import json
import subprocess
import time

with open('data2.json','r') as infile:
    data = json.load(infile)
print(len(data))

start = time.time()
i = 0
toEncrypt = ''
reference = {}
for x in data:
    toEncrypt += x
    reference[i] = x
    i += 1
print('Finished concatenating')
exit()
encrypted = subprocess.run(['encrypt.exe',toEncrypt],stdout=subprocess.PIPE).stdout.decode('utf-8')[:-2]
print('Finished encrypting')
encryptedData = {}
for x in range(len(encrypted)//16-1):
    encryptedData[encrypted[x*16:x*16+16]] = x
end = time.time()
print('Took',end-start,'seconds')
print('Finished separating')

if '903408ec4d951acf' in encryptedData:
    index = encryptedData['903408ec4d951acf']
    print(index)
    print(reference[index])
    print('Found it!')
print('Finished looking')
