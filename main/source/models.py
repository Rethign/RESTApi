# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.db import models
from .randnum import *
#from numpy import random
#from django.db.models.signals import post_save
#from django.contrib.auth.models import User
#from rest_framework.authtoken.models import Token
#from django.dispatch import receiver


class RandNum(models.Model):
#	author = models.CharField(max_length = 255)
	owner = models.ForeignKey('auth.User', related_name = 'randnum', on_delete=models.CASCADE)
	dim = models.IntegerField()
	count_of_num = models.IntegerField()
	rand_list = models.CharField(max_length = 1000)
	fact = models.CharField(max_length = 1000000)
	def __str__(self):
		return "{}".format(self.owner)
	

#@receiver(post_save, sender = User)
#def create_auth_token(sender, instance = None, created = False, **kwargs):
#	if created:
#		Token.objects.create(user = instance)

# Create your models here.
class TestClass(object):
		
	def __init__(self, dim, count_of_num):
		self.test_uni = create_uni(dim, count_of_num)
		self.test_fact = create_fact(dim, count_of_num)
		