
import re

box=[]

def ksa (key,box):
    for i in range(256):
        box.append(i)
    j = 0
    for i in range (256):
        j = (j + box[i] + key[i % len(key)]) % 256
        box[i],box[j] = box[j], box[i]

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
            box = []
            
            ksa(sessionKey,box)

            i = 1 % 256
            j = (box[i]) % 256

            box[i],box[j] = box[j], box[i]
            keyStreamByte = box[(box[i] + box[j]) % 256]

            cipherByte = (int("aa", 16)) ^ keyStreamByte
            values.append([str(iv[0]),str(iv[1]),str(iv[2]),str(cipherByte)])
    return values
    
def RecoverKey(values):
    keyLength = int(values[-1][0]) - 2
    key = [None] * 3
    for A in range(keyLength):
        prob = [0] * 256
        for row in values:
            key[0] = int(row[0])
            key[1] = int(row[1])
            key[2] = int(row[2])

            j = 0
            box = []
            for i in range(256):
                box.append(i) 

            for i in range(A + 3):
                j = (j + box[i] + key[i]) % 256
                box[i],box[j] = box[j],box[i]
                if i == 1:
                    original0 = box[0]
                    original1 = box[1]

            i = A + 3
            z = box[1]
            if z + box[z] == A + 3:
                if (original0 != box[0] or original1 != box[1]):
                    continue
                keyStreamByte = int(row[3]) ^ int("aa", 16)
                keyByte = (keyStreamByte - j - box[i]) % 256
                prob[keyByte] += 1
            higherPossibility = prob.index(max(prob))
        key.append(higherPossibility)

    userInput = key[3:]
    result = [format(key, 'x') for key in userInput]
    rawkey = ''.join(result).upper()
    print("Result: ", rawkey)
    
key = "EB5723"
print("This is the key: ", key)
v = Output(key)
if (v == 0):
    print("Value Not A Hex")
else:
    print("Starting the attempt to decode")
    RecoverKey(v)
