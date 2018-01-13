from numpy import *

'''
def rand(serializer):
	a = serializer.validated_data.get('max_val')
	b = serializer.validated_data.get('count_of_num')
#	c = random.randint(a, size = (1, b))
	c = random.uniform(-1.0, 1.0, size = b)
	return c
'''		

def create_uni(dim, len):
	c = ""
	tmp = []

	for i in range(0,dim):
        	tmp.append( random.uniform(-1.0, 1.0, len))
	for i in range(0, len):
        	c += '('
        	for j in range(0, dim):
	                c += str(tmp[j][i])
        	        if(j != (dim-1)):
	                         c += ', '
        	c += '); '
	return c


def create_fact(dim, len):
	conds = power(len, dim)
	
	H = zeros((conds, dim))
	rang = conds
	tmp = 0
	for j in range(dim):
        	tmp = 0
        	rang //= len
        
        	for i in range(len):
                	x = -1.0 + i*(2.0/(len-1))
                	H[tmp:tmp + (j+1)*rang, j] = x
                	tmp += rang

	        mult = (power(len, j) - 1)
       		for i in range(1, mult+1):
                	H[i*rang*len:(i+1)*rang*len,j] = H[:rang*len, j]

	return H
