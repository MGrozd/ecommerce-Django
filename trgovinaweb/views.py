from django.shortcuts import render
from trgovinaweb.models import *
from trgovinaweb.forms import *
from django.http import *
import time

# Create your views here.
def index(request):
	t = time.localtime()
	s = '{}:{}:{}'.format(t[3], t[4], t[5])
	podatci = {'vrijeme':s}
	return render(request,'index.html',podatci)

def proizvodi_index(request):
	data = Proizvod.objects.all().order_by('Ime')
	podatci = {'data':data}
	return render(request,'proizvodi_index.html',podatci)

def proizvodi_add(request):
	if request.method == 'POST':
		data = ProizvodForm(request.POST)
		if (data.is_valid()):
			data.save()
			return HttpResponseRedirect('/trgovinaweb/proizvodi/')
		else:
			return render(request, 'proizvodi_form.html', {'form':data})
	else:
		form = ProizvodForm()
		return render(request, 'proizvodi_form.html',{'form':form})

def proizvodi_edit(request,ID):
	data = Proizvod.objects.filter(id=ID)
	if len(data) == 0:
		return render(request, 'greska.html', {'opis':'proizvod ne postoji'})
	p = data[0]
	if request.method == 'POST':
		pr = ProizvodForm(request.POST, instance=p)
		if pr.is_valid():
			pr.save()
			return HttpResponseRedirect('/trgovinaweb/proizvodi/')
		else:
			return render(request, 'proizvodi_form.html',{'form':pr})
	else:
		form = ProizvodForm(instance=p)
		return render(request, 'proizvodi_form.html', {'form':form})

def proizvodi_delete(request, ID):
	proizvod = Proizvod.objects.filter(id=ID)[0]
	if request.method == 'POST':
		proizvod.delete()
		return HttpResponseRedirect('/trgovinaweb/proizvodi/')
	else:
		form = ProizvodDelete(instance=proizvod)
		return render(request, 'proizvodi_delete.html', {'form':form, 'proizvod':proizvod})
