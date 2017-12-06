import numpy
from pyDOE import *

dim = 3
len = 6

conds = numpy.power(len, dim)

H = numpy.zeros((conds, dim))
rang = conds
tmp = 0
for j in range(dim):
	tmp = 0
	rang //= len
	#z = const
	for i in range(len):
		x = -1.0 + i*(2.0/(len-1))
		H[tmp:tmp + (j+1)*rang, j] = x
		tmp += rang

	mult = (numpy.power(len, j) - 1)
	for i in range(1, mult+1):
		H[i*rang*len:(i+1)*rang*len,j] = H[:rang*len, j]
		#H[i*rang:(i+1)*rang, j] = H[:rang, j]


#print H
