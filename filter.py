
import json
import re

words = {}
with open("words_dictionary.json",'r') as infile:
    data = json.load(infile)
    print(len(data))

with open('english2.txt','r') as infile:
    for line in infile:
        word = line[:-1]
        if 4 <= len(word) <= 8:
            words[word] = None
    
print(len(words))

regex = r"[^0-9`~!@#$%^&*()+\-_=[{\]}\\|'<,.>?/\";:£§º©®\s]{1,}[・.。][^0-9`~!@#$%^&*()+\-_=[{\]}\\|'<,.>?/\";:£§º©®\s]{1,}[・.。][^0-9`~!@#$%^&*()+\-_=[{\]}\\|'<,.>?/\";:£§º©®\s]{1,}"
print(re.findall(regex,'a.a.a'))

print(len(words))
w3w = {}
for a in words:
    if a[:8] not in w3w and a[:7]+'.' not in w3w:
        for b in words:
            address = (a+'.'+b)[:8]
            if address not in w3w and len(address) == 8:
                w3w[address] = 1
with open('data1.json','w') as f:
    json.dump(w3w,f)
print(len(w3w))
