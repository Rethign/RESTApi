from rest_framework import serializers
from .models import RandNum

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
