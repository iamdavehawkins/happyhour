from django.contrib.auth.models import User
from django import forms

from models import HappyHour, TIME_CHOICES

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class HappyHourForm(forms.ModelForm):
	'''
	Primary form to add a new happy hour

	TODO: Consider which fields are req'd and which aren't
		  Also some custom validators should be added
			- at least one day must be checked
			- at least one (drinks or food must be checked)
	'''
	name = forms.CharField(max_length=200, 
						   widget=forms.TextInput(attrs={'placeholder':"Bar / Restaurant Name"})
						   )
	notes = forms.CharField(max_length=200,
							widget=forms.Textarea(attrs={'placeholder':'Enter details for this happy hour \
									   					 (e.g. $2 Pints, Half off appetizers)'})
							)
	start_time = forms.ChoiceField(choices=TIME_CHOICES)
	end_time = forms.ChoiceField(choices=TIME_CHOICES)
	# Boolean fields are a little weird in Django, they initialize to null?
	# 	and if required=True, they MUST be checked by the user or the form is invalid
	monday = forms.BooleanField(required=False, initial=False)
	tuesday = forms.BooleanField(required=False, initial=False)
	wednesday = forms.BooleanField(required=False, initial=False)
	thursday = forms.BooleanField(required=False, initial=False)
	friday = forms.BooleanField(required=False, initial=False)
	saturday = forms.BooleanField(required=False, initial=False)
	sunday = forms.BooleanField(required=False, initial=False)
	food = forms.BooleanField(required=False, initial=False, label='Food specials?')
	drink = forms.BooleanField(required=False, initial=False, label='Drink Specials?')
	city = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder':'e.g. Ann Arbor'}))

	class Meta:
		model = HappyHour
		fields = ('name', 'notes', 'start_time', 'end_time',
			'monday', 'tuesday', 'wednesday', 'thursday',
			'friday', 'saturday', 'sunday', 'food', 'drink', 'city')
		exclude = ['user']
