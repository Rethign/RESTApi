from rest_framework import serializers
from .models import RandNum

class RandNumSerializer(serializers.ModelSerializer):

	owner = serializers.ReadOnlyField(source = 'owner.username')
	rand_list = serializers.ReadOnlyField()

	class Meta:
		model = RandNum
		fields = ('id', 'owner', 'max_val', 'count_of_num', 'rand_list')
