from django import forms
from base.models import Cadastro

#A classe cadastro herda de forms.Form. Isso faz que ela herde características dos formulários do django
#Essas funções de input fazem validações, ex: email precisa de @, senha precisa de x caracteres etc

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'senha']
        widgets = { 'senha': forms.PasswordInput()}
        #O django vai fazer a validação do mesmo jeito com base nas funções que você colocou no models 

#Forma antiga: 
# class CadastroForm(forms.Form):
#     nome= forms.CharField()  
#     email= forms.EmailField()
#     senha= forms.CharField(widget= forms.PasswordInput)