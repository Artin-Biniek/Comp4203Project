from RC4 import *

key = "temp"
plaintext = "test"
test = rc4Encrypt(plaintext,key)
print(test)
print(rc4Decrypt(test,key))

#Testing FMS.py function
keySteam=""
output=""
box=""
plain="Test message"


ksa(key,plain)
print(prga(plain, box, keyStream, output))