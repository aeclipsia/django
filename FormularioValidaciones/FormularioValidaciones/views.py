from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from FormularioValidaciones.forms import ContactForm

@csrf_exempt
def incidencia(request):
    if request.method=="POST":
        miFormulario=ContactForm(request.POST)
        if miFormulario.is_valid():
            email=miFormulario.cleaned_data['email']
            mensaje=miFormulario.cleaned_data['mensaje']
            dicc={'email':email,'mensaje':mensaje}
            return render(request,'datos.html',dicc)
    else:
        miFormulario=ContactForm()
    return render(request,'home.html',{'form':miFormulario})