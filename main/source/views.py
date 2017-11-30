# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
import randnum, json
from .serializers import RandNumSerializer
from .models import RandNum

# Create your views here.

class RandNumCreateView(generics.ListCreateAPIView):
	queryset = RandNum.objects.all()
	serializer_class = RandNumSerializer

	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)
		c = randnum.rand(serializer)
		serializer.save(rand_list = str(c))

class RandNumDetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = RandNum.objects.all()
	serializer_class = RandNumSerializer

