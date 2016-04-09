#coding:utf-8
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.





class Classify(models.Model):
	name = models.CharField(max_length=128,unique=True)

	def __unicode__(self):
		return self.name

class Commodity(models.Model):
	#id=models.CharField(max_length=128,unique=True)
	name=models.CharField(max_length=128,unique=True,primary_key=True)
	brand=models.CharField(max_length=128)
	classify=models.ForeignKey(Classify)
	price=models.IntegerField()

	def __unicode__(self):
		return self.name


class UserProfile(models.Model):
	user=models.OneToOneField(User)
	phone=models.CharField(max_length=128,unique=True)
	picture = models.ImageField(upload_to='profile_images',blank=True)
	#cart = models.OneToOneField(Commodity)

	def __unicode__(self):
		return self.user.username