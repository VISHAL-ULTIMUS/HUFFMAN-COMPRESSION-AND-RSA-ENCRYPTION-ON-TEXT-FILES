import os
import sys
from RSA import *

if(os.path.exists(sys.argv[1])):
        with open(sys.argv[1], 'r') as f1:
            l = f1.read()
            l2 = l.split()
            d = l2[0]
            n = l2[1]

decrypt = []
en = l2[2:]
for i in range(len(en)):
    decrypt.append(decode(int(en[i]),int(d),int(n)))

output = ""

for i in decrypt:
    output += str(i)

with open("output.txt", 'w') as f:
    f.write(output)
