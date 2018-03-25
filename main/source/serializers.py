from rest_framework import serializers
from .models import Plan

choices = {
	'Identical',
	'Individual'
}

class ChoiceSerializer(serializers.Serializer):
	Random = serializers.BooleanField()
	Uniform = serializers.BooleanField()
	Factorial = serializers.BooleanField()
	Latin_HyperCube = serializers.BooleanField()
	Halton = serializers.BooleanField()
	Sobol = serializers.BooleanField()
	Plan_type = serializers.ChoiceField(choices)

class PlanSerializer(serializers.Serializer):
	#declaration of sample count
	dim = serializers.IntegerField(min_value = 1)
	count_of_num = serializers.IntegerField(min_value = 1)

	#declaration of plan types
	planType = serializers.ReadOnlyField()
	plan = Plan(plan_type='lhs')

	def create(self, data):
		print("PlanSerializer constructor")
		return self.plan

	def update(self, data):
		print("PlanSerializer update")
		self.result = self.plan.update(data)
		return self.result