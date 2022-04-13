box=[]

def createBox(box):
    for i in range(256):
        box.append(i)

def ksa (key,box):
    createBox(box)
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
    output = ""
    for i in range(len(plain)):
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        swap(box,i,j)

        keyStreamByte = box[(box[i] + box[j]) % 256]
        keyStream += chr( keyStreamByte)
        # print(chr(ord(plain[i-1])^keyStreamByte))
    return keyStream #output
    
def swap(box,a,b):
    temp = box[a]
    box[a] = box[b]
    box[b] = temp


def temp  (plain):
    eplain = bytes(plain, 'utf-8')
    ehex = eplain.hex()

    key =[]
    i = 0
    while i < len(ehex):
        key.append(int(ehex[i] + ehex[i+1], 16))
        i += 2
    
    iv = [3, 255, 0]
    sessionKey = iv + key

    for A in range(len(key)):
        iv[0] = A+3
        for j in range(256):
            iv[2] = j
            sessionKey = iv + key
            box = []
            ksa(sessionKey,box)
            



    

    
temp("AF1423")