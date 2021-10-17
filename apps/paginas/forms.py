from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuário', required=True)
    #senha = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput())
    senha = forms.CharField(label='Senha', required=True)
