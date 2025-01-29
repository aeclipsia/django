from django.http import HttpResponse
from django.shortcuts import render
from Practica10.forms import *
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.POST:
        form=Formulario(request.POST)
        if form.is_valid():
            collection=form.cleaned_data
            return render(request,'details.html',collection)
    else:
        form=Formulario()
    return render(request,"index.html",{'form':form})