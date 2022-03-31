from RC4 import *

key = "temp"
plaintext = "test"
test = rc4Encrypt(plaintext,key)
print(test)
print(rc4Decrypt(test,key))