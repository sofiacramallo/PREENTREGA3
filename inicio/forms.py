from django import forms 
class crearAutoFormulario(forms.Form): 
    modelo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)

