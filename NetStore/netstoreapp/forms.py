#coding:utf-8
from django import forms
from django.contrib.auth.models import User
from netstoreapp.models import UserProfile,Classify,Commodity

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('phone','picture')

class ClassifyForm(forms.ModelForm):

	class Meta:
		model=Classify
		fields=('name',)


class CommdityForm(forms.ModelForm):
	class Meta:
		model=Commodity
		fields=('name','brand','classify','price')