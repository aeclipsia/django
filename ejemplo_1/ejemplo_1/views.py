from django.http import HttpResponse
from django.shortcuts import render



def saluda(request):
    # return HttpResponse("Hola DAW2")
    contexto={'nombre':'Jared','mensaje':'HEYA'}
    # return render(request,'index.html',contexto)
    return render(request,'index.html',)

def despedida(request):
    return render(request,'adios.html')

def tuEdadFutura(request,e):
    e+=10
    return render(request,'edad.html',{'edad':e})