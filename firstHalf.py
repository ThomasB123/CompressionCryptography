
import os
import json
import subprocess

with open('data2.json','r') as infile:
    data = json.load(infile)
print(len(data))

for x in data:
    encrypted = subprocess.run(['encrypt.exe',x],stdout=subprocess.PIPE).stdout.decode('utf-8')[:-2]
    if encrypted == '903408ec4d951acf':
        print(x)
        print(encrypted)