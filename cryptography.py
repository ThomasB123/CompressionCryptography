# 90 34 08 ec 4d 95 1a cf ae b4 7c a8 83 90 c4 75
# what 3 words. lowercase words seperated by full stops
# heavy.bravo.goals is Max's office E321
# not marked for novelty, marked for efficiency

from des import DesKey # this is what he is using
from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes
import string
import random
import re
import os

m = b'0123456789abcdef'
m.hex()
k = b'DUCrypto' # if key is correct then output will be a80f2c74f235484
key = DesKey(k)
c = key.encrypt(m)
print(c)
print(c.hex()) # a80f2c74f235484 if using correct key

print(c.hex() == 'a80f2c74f235484')
'''4c7...'''

'''
key = b'-8B key-'
cipher = DES.new(key,DES.MODE_ECB)
plaintext = b'heavy.bravo.goal'#s'
msg = cipher.encrypt(plaintext)
print(msg)
integer = int.from_bytes(msg,'big')
print(integer)
hexi = hex(integer)
print(hexi)
#print(hexi == 0x903408ec4d951acfaeb47ca88390c475)
print(hexi == '0x95fa49223b1e30d0')
'''
# hexi = 0x903408ec4d951acfaeb47ca88390c475
# hexi is 32 characters long, so 16 bytes, so plaintext is 16 characters, so w3w musy be at least 9 is using padding

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

'''
print(bytes.fromhex(hexi[2:]))
#print(bytes.fromhex('903408ec4d951acfaeb47ca88390c475'))
cipherbytes = bytes.fromhex(hexi[2:])
cipherbytes = bytes.fromhex('903408ec4d951acfaeb47ca88390c475')
plain = cipher.decrypt(cipherbytes)
print(plain.decode())


outcome = 0x903408ec4d951acfaeb47ca88390c475
print(int(outcome))
key = DesKey(b'some key')
encrypted = key.encrypt(b'any long message')
print(encrypted)
decrypted = key.decrypt(encrypted)
print(decrypted)
'''