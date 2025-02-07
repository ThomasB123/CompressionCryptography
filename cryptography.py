# 90 34 08 ec 4d 95 1a cf ae b4 7c a8 83 90 c4 75
# what 3 words. lowercase words seperated by full stops
# heavy.bravo.goals is Max's office E321
# not marked for novelty, marked for efficiency

from des import DesKey # this is what he is using
#from Cryptodome.Cipher import DES
#from Cryptodome.Random import get_random_bytes
import string
import random
import re
import os

def encryptHex(hexString,k):
    m = bytes.fromhex(hexString)
    key = DesKey(k)
    c = key.encrypt(m)
    c = c.hex()
    print(c)
    return c

hexString = '1000000000000001'#0000000000000001'
k = b'00000000'
encryptHex(hexString,k)

#string = 'heavy.br'
#m = bytes(string,'utf8')
#print(m.hex())
#k = b'12345678' # if key is correct then output will be a80f2c74f235484
#key = DesKey(k)
#c = key.encrypt(m)
#print(c.hex()) # a80f2c74f235484 if using correct key

#print(c.hex() == 'a80f2c74f235484e')
#'''4c7...'''

# hexi = 0x903408ec4d951acfaeb47ca88390c475
# hexi is 32 characters long, so 16 bytes, so plaintext is 16 characters, so w3w musy be at least 9 is using padding

# brute force approach:
'''
regex = r"^/*[^0-9`~!@#$%^&*()+\-_=[{\]}\\|'<,.>?/\";:£§º©®\s]{1,}[・.][^\s]{1,}[・.][^\s]{1,}$"
i = 0
while True:
    key = os.urandom(8)
    #print(key)
    #alphabet = string.ascii_letters + string.digits #+ string.punctuation
    #key = ''.join(random.choice(alphabet) for i in range(8))
    #key = key.encode()
    cipher = DES.new(key,DES.MODE_ECB)
    cipherbytes = bytes.fromhex('903408ec4d951acfaeb47ca88390c475')
    try:
        i += 1
        plain = cipher.decrypt(cipherbytes).decode()
        if re.search(regex,plain,flags=re.UNICODE):#match('^(a-z)...]',plain):
            #if re.search("[a-z.]",plain):#match('^(a-z)...]',plain):
            break
        print(i)
    except UnicodeDecodeError:
        pass
print('Found Key: {}'.format(key))
print('Found plaintext: {}'.format(plain))
'''