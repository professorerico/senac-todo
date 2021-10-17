from django import forms

from .models import Categoria, Tarefas

class CategoriaForm(forms.ModelForm) :
    class Meta:
        model = Categoria
        fields = '__all__'
        # fields = ['nome', 'descricao']
        # exclude = ['descricao]

class TarefaForm(forms.ModelForm) :
    class Meta:
        model = Tarefas
        fields = '__all__'