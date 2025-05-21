from django import forms
from .models import quarto, Atendente

class quartoForms(forms.ModelForm):
    class Meta:
        model = quarto
        fields = ['num_Quarto','qtd_Hospedes','tipo','valor','descricao','status', 'img']

class AtendenteForms(forms.ModelForm):
    class Meta:
        model = Atendente
        fields = ['username', 'password']

    def form_valid(self, form):

        form.cleaned_data['grupo'] = Atendente
        return super().form_valid(form)