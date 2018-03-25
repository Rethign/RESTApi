# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponseRedirect
import json
from rest_framework import views, viewsets, status
from rest_framework.response import Response

from .serializers import *
from .plans import *

class ChoiceView(viewsets.ViewSet):
	serializer_class = ChoiceSerializer
	def list(self, request):
		helloString = "Welcome to the server. Choose your plan."
		print("ChoiceView.list()")
		return Response(helloString)
	
	def create(self, request):
		print("ChoiceView.print()")
		choice = request.data.get('Plan_type', None)
		print(choice)
		setFlags(request.data)
		if choice == "Individual":
			return HttpResponseRedirect(redirect_to='/plan')
		elif choice == "Identical":
			return HttpResponseRedirect(redirect_to='/plan')
		else:
			return Response(None, status = status.HTTP_400_BAD_REQUEST)


class PlanView(viewsets.ViewSet):
	serializer_class = PlanSerializer
	serializer = PlanSerializer()
	def list(self, request):
		print("PlanView.list()")
		helloString = "Enter count of dimentions and samples"
		return Response(helloString)

	def create(self, request):
		ret = checkValid(request.data)
		if ret == True:
			self.serializer.update(data=request.data)
			print("PlanView.create()")
			return Response(self.serializer.result, status = status.HTTP_201_CREATED)
		else:
			helloString = "Wrong data inserted, please check the data."
			return Response(helloString, status = status.HTTP_400_BAD_REQUEST)
