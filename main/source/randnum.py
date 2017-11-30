from .serializers import RandNumSerializer
from numpy import random


def rand(serializer):
	a = serializer.validated_data.get('max_val')
	b = serializer.validated_data.get('count_of_num')
	c = random.randint(a, size = (1, b))
	return c
