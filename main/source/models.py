# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.db import models
from .plans import *
import copy
from matplotlib.pyplot import *


class Plan(object):
	plan = flags.copy()

	def __init__(self, **kwargs):
		self.plan_type = kwargs.get('plan_type', None)
		print("Plan constructor")

	def update(self, data):
		print("Plan update")
		for field, value in data.items():
			setattr(self, field, value)
		self.dim = int(self.dim)
		self.count_of_num = int(self.count_of_num)
		self.generate()
		return self.plan

	def generate(self):
		x = []
		print("Creating plan " + str(self.plan_type))
		if flags.get("Latin_HyperCube") == True:
			self.plan["Latin_HyperCube"] = createLhs(self.dim, self.count_of_num)
		if flags.get("Random") == True:
			self.plan["Random"] = createSimple(self.dim, self.count_of_num, "Rand")
			x = np.swapaxes(self.plan["Random"], 0, 1)
			plot(x[0], x[1], 'ro')
			show()
		if flags.get("Uniform") == True:
			self.plan["Uniform"] = createUni(self.dim, self.count_of_num, "Uni")
		if flags.get("Factorial") == True:
			self.plan["Factorial"] = createFact(self.dim, self.count_of_num)
		if flags.get("Halton") == True:
			self.plan["Halton"] = createHalton(self.dim, self.count_of_num)
			x = np.swapaxes(self.plan["Halton"], 0, 1)
			plot(x[0], x[1], 'bo')
			show()
		if flags.get("Sobol") == True:
			self.plan["Sobol"] = createSobol(self.dim, self.count_of_num)
			x = np.swapaxes(self.plan["Sobol"], 0, 1)
			plot(x[0], x[1], 'go')
			show()
		return self.plan



