# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
import json

from .serializers import RandNumSerializer, TestSerializer
from .models import RandNum
from .testclass import TestClass
from rest_framework import views, viewsets, status
from rest_framework.response import Response

# Create your views here.
tests = {
	1:	TestClass(id = 1, dim = 2, count_of_num = 2),
	2:	TestClass(id = 2, dim = 3, count_of_num = 2),
	3:	TestClass(id = 3, dim = 3, count_of_num = 500),
}

def get_id():
	return max(tests) + 1


class RandNumCreateView(generics.ListCreateAPIView):
	queryset = RandNum.objects.all()
	serializer_class = RandNumSerializer

	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)
		create_rand(serializer)

class RandNumDetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = RandNum.objects.all()
	serializer_class = RandNumSerializer

class TestView(viewsets.ViewSet):
	serializer_class = TestSerializer

	def list(self, request):
		serializer = TestSerializer(
			instance=tests.values(), many = True)
		return Response(serializer.data)

	def create(self, request):
		serializer = TestSerializer(data=request.data)
		if serializer.is_valid():
			test = serializer.save()
			test.id = get_id()
			tests[test.id] = test
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

