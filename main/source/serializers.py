from rest_framework import serializers
from .models import RandNum, TestClass
from .randnum import *
from .testclass import *

from rest_framework.response import Response
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

	dim = serializers.IntegerField()
	count_of_num = serializers.IntegerField()
	
	test_fact = serializers.ListField(
		child = serializers.FloatField(min_value = -1.0, max_value = 1.0)
	)
	test_fact = serializers.ReadOnlyField()
	
	test_uni = serializers.ListField(
		child = serializers.FloatField(min_value = -1.0, max_value = 1.0)
	)
	test_uni = serializers.ReadOnlyField()
	def create(self, validated_data):
		return TestClass(id=None, **validated_data)
	
	def update(self, instance, validated_data):
		for field, value in validated_data.items():
			setattr(instance, field, value)
		return instance

