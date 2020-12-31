
import json
import re

words = {}
with open("words_dictionary.json",'r') as infile:
    data = json.load(infile)
    print(len(data))

with open('english2.txt','r') as infile:
    for line in infile:
        word = line[:-1]
        if 4 <= len(word) <= 6 and "'" not in word:
            words[word] = None

with open('english.txt','w') as outfile:
    for word in words:
        outfile.write(word+'\n')
    
print(len(words))

regex = r"[^0-9`~!@#$%^&*()+\-_=[{\]}\\|'<,.>?/\";:£§º©®\s]{1,}[・.。][^0-9`~!@#$%^&*()+\-_=[{\]}\\|'<,.>?/\";:£§º©®\s]{1,}[・.。][^0-9`~!@#$%^&*()+\-_=[{\]}\\|'<,.>?/\";:£§º©®\s]{1,}"
print(re.findall(regex,'a.a.a'))

print(len(words))
w3w = {}
bil = ['bile','bilge','bilges','bilked','bill','billed','billet','billow','bills','billy']
for a in bil:
    for b in words:
        if len(a+b) == 10:
            address = (a+'.'+b)[-8:]
            if address not in w3w:
                w3w[address] = 1
                #w3w[bytes(address,'utf8').hex()] = 1
with open('data3.json','w') as f:
    json.dump(w3w,f)
print(len(w3w))
