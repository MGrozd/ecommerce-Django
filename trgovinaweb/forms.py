from django.forms import ModelForm
from trgovinaweb.models import *

class  ProizvodForm(ModelForm):
	class Meta:
		model = Proizvod
		fields = '__all__'
		error_messages = {'Ime':{'required':'Ime je obavezno'},
		'Kod':{'required':'Kod je obavezan'},
		'Cijena':{'required':'Cijena je obavezna'}}

class ProizvodDelete(ModelForm):
	class Meta:
		model = Proizvod
		fields = ['id']
	#id = forms.IntegerField(widget=forms.HiddenInput())
