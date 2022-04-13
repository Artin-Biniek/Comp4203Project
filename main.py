from RC4 import *
from FMS import *
key = "temp"
plaintext = "test"
test = rc4Encrypt(plaintext,key)
print(test)


#Testing FMS.py function
keyStream=""
output=""

plain="Test message"

# keyStream=ksa_string(key,plain)

print(keyStream)
# print(prga(plain,keyStream))