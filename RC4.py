from RC4Encryption import RC4Encryption

def rc4Encrypt(plaintext,key):
    k = bytes(key, 'utf-8')
    rc4 = RC4Encryption(k)
    rc4.make_key()
    print("Key Length 1",rc4.key_length)
    
    plain = bytes(plaintext, 'utf-8')
    en = rc4.crypt(plain)
    print("Key Length 2",rc4.key_length)
    return en

def rc4Decrypt(ciphertext,key):
    k = bytes(key, 'utf-8')

    rc4 = RC4Encryption(k)
    rc4.make_key()
    return rc4.crypt(ciphertext).decode('utf-8')

key = "keys"
test = rc4Encrypt("plaintext",key)