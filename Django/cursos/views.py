from django.shortcuts import render
from cursos.forms import CursoForm
from django.views.decorators.cache import cache_page 
from cursos.models import Curso

# A view vai criar a função que vai se comunicar com o Banco de Dados
@cache_page(30)
def criar_curso(request):
    #pesquisa todos os objetos que tem 
    cursos = Curso.objects.all()
    form = CursoForm(request.POST or None)
    sucesso = False
    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'form': form,
        'sucesso': sucesso,
        'cursos': cursos
    }
    return render(request, 'criar_curso.html', contexto)