
import json

with open('data1.json','r') as infile:
    data = json.load(infile)
print(len(data))

hexi = {}
for x in data:
    hexi[bytes(x,'utf8').hex()] = 1

with open('data2.json','w') as f:
    json.dump(hexi,f)
print(len(hexi))