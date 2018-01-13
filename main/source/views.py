# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
import json

from .serializers import RandNumSerializer, TestSerializer
from .models import RandNum, TestClass

from .randnum import *
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

class TestView(generics.ListCreateAPIView):
	queryset = RandNum.objects.all()
	serializer_class = TestSerializer
	
	def perform_create(self, serializer):
		serializer.save()
		