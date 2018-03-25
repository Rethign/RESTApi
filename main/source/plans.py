import numpy as np
from pyDOE import *
import sobol_seq

MAX_VALUE = 65536

flags = {
	'Latin_HyperCube':	False,
	'Random':			False,
	'Uniform':			False,
	'Factorial':		False,
	'Halton':			False,
	'Sobol':			False
}

def setFlags(info):
	for field, value in flags.items():
		flags[field] = False
	for field, value in info.items():
		if flags.get(field, None) != None:
			if value == "true":
				flags[field] = True
	print(flags)


def checkValid(data):
	print("Check validation data")

	cnt = data.get('count_of_num', None)
	print(cnt)
	if not(cnt.isdigit()):
		return False
	cnt = int(cnt)
	dim = data.get('dim', None)
	if not(dim.isdigit()):
		return False
	dim = int(dim)

	if flags.get("Factorial") == True:
		result = power(cnt, dim)
	else:
		result = dim*cnt

	print("HelloThere" + str(result))

	if (result > MAX_VALUE) or (result <= 0):
		return False
	else:
		return True

def createSimple(dim, len, plan):
	tmp = []
	out = []
	
	if( plan == "Uni"):
		for i in range(0,dim):
			out.append( np.random.uniform(-1.0, 1.0, len))
		out = np.swapaxes(out, 0, 1)
	else:
		out = np.random.rand(len, dim)
		out = -1.0 + out*2
	return out
	
def createFact(dim, len):
	conds = power(len, dim)
	
	H = zeros((conds, dim))
	rang = conds
	tmp = 0
	for j in range(dim):
		tmp = 0
		rang //= len
		for i in range(len):
			if(len != 1):
				x = -1.0 + i*(2.0/(len-1))
			else:
				return 0
			H[tmp:tmp + (j+1)*rang, j] = x
			tmp += rang
		mult = (power(len, j) - 1)
		for i in range(1, mult+1):
			H[i*rang*len:(i+1)*rang*len,j] = H[:rang*len, j]
	return H

def createLhs(dim, len):
	if len == 1:
		latin = []
		for val in range(0, dim):
			latin.append(0)
	else:
		latin = lhs(dim, samples = len, criterion = "cm")
		latin = -1.0 + latin*2
	return latin

def nextPrime():
	def isPrime(num):
		for i in range(2, int (num**0.5)+1):
			if(num % i) ==0:
				return False
			return True
	prime = 3
	while(1):
		if isPrime(prime):
			yield prime
		prime += 2
		
def vdCorput(n, base=2):
	vdc, denom = 0, 1
	while n:
		denom *= base
		n, reminder = divmod(n, base)
		vdc += reminder/float(denom)
	return vdc
	
def createHalton(dim, size):
	seq = []
	primeGen = nextPrime()
	next(primeGen)
	for d in range(dim):
		base = next(primeGen)
		seq.append([vdCorput(i, base) for i in range(size)])
	seq = np.swapaxes(seq, 0, 1)
	seq = -1.0 + seq*2
	return seq
	
def createSobol(dim, size):	
	return sobol_seq.i4_sobol_generate(dim, size)