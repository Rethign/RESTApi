# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
import json
from .randnum import *
from .serializers import RandNumSerializer
from .models import RandNum

# Create your views here.

class RandNumCreateView(generics.ListCreateAPIView):
	queryset = RandNum.objects.all()
	serializer_class = RandNumSerializer

	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)
		create_rand(serializer)

class RandNumDetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = RandNum.objects.all()
	serializer_class = RandNumSerializer

