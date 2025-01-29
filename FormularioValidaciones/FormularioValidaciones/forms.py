from django import forms

class ContactForm(forms.Form):
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'noreply@example.com',
                                                         'class':'form-control'}))
    INCIDENCIAS=[('software', 'Software'),
                ('hardware', 'Hardware' ),
                ('red', 'Conexión a internet')]
    incidencia=forms.ChoiceField(choices=INCIDENCIAS,widget=forms.Select(attrs={'class':'form-control'}))
    mensaje=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    

    def clean_mensaje(self):
        mensaje=self.cleaned_data['mensaje']
        if len(mensaje.split())<5:
            raise forms.ValidationError("No son suficientes palabras.Por favor, especifique más")
        return mensaje