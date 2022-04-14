
import re

box=[]



def something (key,box):
    for i in range(256):
        box.append(i)
    j = 0
    for i in range (256):
        #if J is less then 2 or if dealing with a non int in the key then skip
        #isinstance(int(key[i%len(key)]),int))
       # print(key[i%len(key)].isdigit())
        if( key[i%len(key)].isdigit() ):
            #print( j + box[i] + int(key[i % len(key)]) )
            if((j + box[i] + int(key[i % len(key)]))>2 ):
                j = (j + box[i] + int(key[i % len(key)])) % 256
                box[i],box[j] = box[j], box[i]
            else:
                #Not sure how to add A+3 here
                j= j-int(key[(ord('A')+3)%len(key)])


def ksa (key,box):
    for i in range(256):
        box.append(i)
    j = 0
    for i in range (256):
        j = (j + box[i] + key[i % len(key)]) % 256
        box[i],box[j] = box[j], box[i]

# #This function encrypts the plaintext and makes it into a byte    
# def ksa_string(plain,key):
#     encode = bytes(key, 'utf-8')
#     ksa(encode,box)
#     keyStream = ""
#     keyStream = prga(plain,keyStream)
#     return keyStream


# def prga(plain,keyStream):
#     i = 0
#     j = 0
#     output = ""
#     for i in range(len(plain)):
#         i = (i + 1) % 256
#         j = (j + box[i]) % 256
#         box[i],box[j] = box[j], box[i]


#         keyStreamByte = box[(box[i] + box[j]) % 256]
#         keyStream += chr(keyStreamByte)
#         # print(chr(ord(plain[i-1])^keyStreamByte))
#     print(keyStream)
#     return keyStream #output

def Output (plain):
    iv = [3, 255, 0]
    values = []

    case = plain.upper()
    check = re.search("[G-Z]",case)

    if(check != None):
        return 0

    key = []
    i = 0
    while i < len(plain):
        key.append(int(plain[i] + plain[i+1], 16))
        i += 2
    
    sessionKey = iv + key

    for A in range(len(key)):
        iv[0] = A+3
        for k in range(256):
            iv[2] = k
            sessionKey = iv + key
            # print(str(sessionKey))
            box = []
            #non ints were detected in the session key
            ksa(sessionKey,box)

            i = 1 % 256
            j = (box[i]) % 256

            box[i],box[j] = box[j], box[i]
            keyStreamByte = box[(box[i] + box[j]) % 256]

            cipherByte = (int("aa", 16)) ^ keyStreamByte
            values.append([str(iv[0]),str(iv[1]),str(iv[2]),str(cipherByte)])
    return values
    
def temp2(values):
    iv = [0] * 3
    keyLength = int(values[-1][0]) - 2
    for A in range(keyLength):
        prob = [0]*256
        for i in range(len(values)):
            iv[0] = values[i][0]
    #         iv[1] = values[i][1]
    #         iv[2] = values[i][2]
        
        
    



 
v = Output("F23456")
if (v == 0):
    print(v)
    print("Value Not A Hex")
else:
    temp2(v)
