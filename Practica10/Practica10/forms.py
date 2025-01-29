from django import forms

class Formulario(forms.Form):
    nombre=forms.CharField(max_length=5,required=True,widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Introduce tu nombre"}),label="Nombre")
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Introduce tu email'}),label="Email")
    edad=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Introduce tu edad'}),label="Edad")
    sexoChoices=[('mujer','Mujer'),('hombre','Hombre')]
    sexo=forms.ChoiceField(choices=sexoChoices,widget=forms.RadioSelect)
    interesesChoices=[('programacion','Programación'),('deporte','Deporte')]
    intereses=forms.ChoiceField(choices=interesesChoices,widget=forms.Select(attrs={'class':'form-control'}),label="Temas de Interés")
    aficionesChoices=[('lectura','Lectura'),('viajar','Viajar'),('deporte','Deporte'),('cine','Cine'),('musica','Musica')]
    aficiones=forms.MultipleChoiceField(choices=aficionesChoices,widget=forms.CheckboxSelectMultiple(),label="Aficiones")