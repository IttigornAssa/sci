from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Author,Research

class AutherForm(ModelForm):
	class Meta:
		model =  Author
		exclude=[]
		
	def __init__(self, *args, **kwargs):
		super(AutherForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))

class ResearchForm(ModelForm):
	class Meta:
		model =  Research
		exclude=[]
		
	def __init__(self, *args, **kwargs):
		super(ResearchForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))