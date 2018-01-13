# includes
from .randnum import *

#declaration of class
class TestClass(object):
	
	def __init__(self, **kwargs):
		for field in ('id', 'dim', 'count_of_num'):
			setattr(self, field, kwargs.get(field, None))
#		self.test_uni = create_uni(self.dim, self.count_of_num)
		self.test_fact = create_fact(self.dim, self.count_of_num)
