from mailbox import NoSuchMailboxError
from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)
    