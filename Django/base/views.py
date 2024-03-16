from django.shortcuts import render
from django.http import HttpResponse
#A biblioteca HttpResponse faz a comunicação com a internet 
from base.forms import CadastroForm
from base.models import Cadastro

# Create your views here.

#request é uma biblioteca
def inicio(request):
    return render(request, 'inicio.html')

#render() vem de renderizar. request = requisição, arquivos que queremos renderizar 


def cadastro(request):
    sucesso = False
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
        #a função save() faz por debaixo dos panos o comando insert
    contexto = {
        'form': form, #fazer o post
        'sucesso': sucesso #enviar uma mensagem de sucesso
    }
    return render(request, 'cadastro.html', contexto)

#Forma "grande":
# def cadastro(request):
#     sucesso = False
#     if request.method == 'GET':
#         form = CadastroForm()
#     else: 
#         form = CadastroForm(request.POST)
#         if form.is_valid():
#             sucesso = True
#             A propriedade cleaned_data é um dicionário, que pega cada campo separadamente. É um atributo do próprio django 
#             nome = form.cleaned_data['nome']
#             email = form.cleaned_data['email']
#             senha = form.cleaned_data['senha']
#             Cadastro.objects.create(nome=nome, email=email, senha=senha)
#     contexto = {
#         'form': form, #fazer o post
#         'sucesso': sucesso #enviar uma mensagem de sucesso
#     }
#     return render(request, 'cadastro.html', contexto)
#Se o método for get ele traz o CadastroForm. Se não, ele adiciona o sujeito. 