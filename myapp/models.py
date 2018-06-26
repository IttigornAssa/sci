from __future__ import unicode_literals
from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=20,null=True)
	email = models.CharField(max_length=20,null=True)

	def __str__(self):
		return "id: {}, {}".format(self.id, self.name)

class Research(models.Model):
	name = models.CharField(max_length=100)
	author = models.ForeignKey('Author',on_delete=models.CASCADE)
	abstract = models.CharField(max_length=500)
	year = models.DateField(auto_now=False, auto_now_add=False)
	etc = models.CharField(max_length=100)

	def __str__(self):
		return "id: {}, {}".format(self.id, self.name)

