from RC4Encryption import RC4Encryption

def rc4Encrypt(plaintext,key):
    k = bytes(key, 'utf-8')
    rc4 = RC4Encryption(k)
    rc4.make_key()
    
    plain = bytes(plaintext, 'utf-8')
    return rc4.crypt(plain)

def rc4Decrypt(ciphertext,key):
    k = bytes(key, 'utf-8')

    rc4 = RC4Encryption(k)
    rc4.make_key()
    return rc4.crypt(ciphertext).decode('utf-8')



key = "key"
test = rc4Encrypt("key",key)