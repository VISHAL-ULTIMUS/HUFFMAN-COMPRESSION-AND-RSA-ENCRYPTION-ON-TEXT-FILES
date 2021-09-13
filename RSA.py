import random
import math


primes = [73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241]


def encode(t,e,n):
	m = convert(t)
	m = pow(m,e)
	m = m % n
	return int(m)
	
def convert(t):
	return ord(t)

def decrypt(m,d,n):
	m = pow(m,d)
	m = m % n
	return int(m)
	
def decode(m,d,n):
	t = decrypt(m,d,n)
	return chr(t)
	
def get_primes(primes,l):
	l[0] = random.choice(primes)
	flag = 1
	while(flag == 1):
		l[1] = random.choice(primes)
		if l[0] != l[1]:
			flag = 0
	
def gcd(a,b):
	gcd = 1
	if a > b:
		n = a
	else: 
		n = b
	for i in range(2,n + 1):
		if a % i == 0 and b % i == 0:
			gcd = i
	return gcd 	

def public_key(psi):
	i = 3
	while(i < psi):
		if gcd(i,psi) == 1:
			break
		i += 1
	return i
	
#def private_key(e,psi):
#	k = 2
#	d = ((k * psi) + 1) / e
#	return d

def findModInverse(a, m):
   if gcd(a, m) != 1:
      return None
   u1, u2, u3 = 1, 0, a
   v1, v2, v3 = 0, 1, m
   
   while v3 != 0:
      q = u3 // v3
      v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
   return u1 % m

def main():
	#message = raw_input("Enter Message that needs to be Encrypted:")
	message = open("example.txt",'r').read()
	l = [0,0]
	get_primes(primes,l)
	p = l[0]
	q = l[1]
	n = p * q
	psi = (p - 1) * (q - 1)
	e = public_key(psi)
	d = findModInverse(e,psi)
	encrypt = []
	for i in range(len(message)):
		encrypt.append(encode(message[i],e,n))
	decrypt = []
	for i in range(len(encrypt)):
		decrypt.append(decode(encrypt[i],d,n))
	print ("Initial Message: " + message)
	print ("Encrypted Message: "),
	enc = ""
	for i in encrypt:
		enc += (str)(i)
	print (enc)
	
	f = open("Encrypted.txt", 'w')
	f.write(str(d) + " ")
	f.write(enc)
	print ("Decrypted Message:"),
	dec = ""
	for i in decrypt:
		dec += (str)(i)
	print (dec)
		

if __name__ == "__main__":
	main()		
