import os
import sys
from RSA import *

primes = [73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
          193, 197, 199, 211, 223, 227, 229, 233, 239, 241]

if (os.path.exists(sys.argv[1])):
    with open(sys.argv[1], 'r') as f1:
        message = f1.read()
        l = [0, 0]
        get_primes(primes, l)
        p = l[0]
        q = l[1]
        n = p * q
        psi = (p - 1) * (q - 1)
        e = public_key(psi)
        d = findModInverse(e, psi)
        encrypt = []
        for i in range(len(message)):
            encrypt.append(encode(message[i], e, n))

else:
    print("File doesn't exist!")
    sys.exit()

enc = ""
for i in encrypt:
    enc += (str)(i) + " "

with open("Encrypted.txt", 'w') as f:
    f.write(str(d) + " ")
    f.write(str(n) + " ")
    f.write(enc)
