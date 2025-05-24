from django import forms
from django.contrib.auth.models import User
from .models import *


class quartoForms(forms.ModelForm):
    class Meta:
        model = quarto
        fields = ['num_Quarto','qtd_Hospedes','tipo','valor','descricao','status', 'img']

class AtendenteForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()  
        }