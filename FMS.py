
def ksa (key,box):
    for i in range(256):
        box.append(i)
    j = 0
    for i in range (256):
        j = (j + box[i] + key[i % len(key)]) % 256
        swap(box,i,j)
    
def ksa_string(plain,key):
    encode = bytes(key, 'utf-8')
    box = []
    ksa(encode,box)
    keyStream = ""
    keyStream = prga(plain, box, keyStream)
    print(keyStream)


def prga(plain,box,keyStream):
    i = 0
    j = 0
    for i in range(len(plain)):
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        swap(box,i,j)
        keyStream += chr(box[(box[i] + box[j]) % 256])
    return keyStream
    
def swap(box,a,b):
    temp = box[a]
    box[a] = box[b]
    box[b] = temp

ksa_string("plain","key")

