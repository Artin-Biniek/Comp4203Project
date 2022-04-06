box=[];

def ksa (key,box):
    for i in range(256):
        box.append(i)
    j = 0
    for i in range (256):
        j = (j + box[i] + key[i % len(key)]) % 256
        swap(box,i,j)

#This function encrypts the plaintext and makes it into a byte    
def ksa_string(plain,key):
    encode = bytes(key, 'utf-8')
    ksa(encode,box)
    keyStream = ""
    keyStream = prga(plain,keyStream)
    return keyStream


def prga(plain,keyStream):
    i = 0
    j = 0
    for i in range(len(plain)):
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        swap(box,i,j)
        keyStream += str(box[(box[i] + box[j]) % 256])
        #output=plain[i-1]^keyStream
    return keyStream #output
    
def swap(box,a,b):
    temp = box[a]
    box[a] = box[b]
    box[b] = temp

ksa_string("plain","key")

