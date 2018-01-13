from rest_framework import serializers
from .models import RandNum, TestClass
from .randnum import *

class RandNumSerializer(serializers.ModelSerializer):

	owner = serializers.ReadOnlyField(source = 'owner.username')
	rand_list = serializers.ReadOnlyField()
	fact = serializers.ListField(
		child = serializers.FloatField(min_value = -1.0, max_value = 1.0)
	)
	fact = serializers.ReadOnlyField()

	class Meta:
		model = RandNum
		fields = ('id', 'owner', 'dim', 'count_of_num', 'rand_list', 'fact')

		
class TestSerializer(serializers.Serializer):

	dim = serializers.IntegerField(write_only = True)
	count_of_num = serializers.IntegerField(write_only = True)
	
	rand_list = serializers.ListField(
		child = serializers.FloatField(min_value = -1.0, max_value = 1.0)
	)
	rand_list = serializers.ReadOnlyField()
	
	fact = serializers.ListField(
		child = serializers.FloatField(min_value = -1.0, max_value = 1.0)
	)
	fact = serializers.ReadOnlyField()

	def create(self, validated_data):
		print ('j')
		return TestClass(**validated_data)
		
	def update(self, instance, validated_data):
		print('c')
		instance.rand_list = create_uni(instance.dim, instance.count_of_num)
		instance.fact = create_fact(instace.dim, instance.count_of_num)
		return instance
	

		
		
