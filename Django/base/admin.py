from django.contrib import admin
from base.models import Cadastro

# Register your models here.
#Quais tabelas o administrador terá acesso?

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    #Essa classe te deixa colocar alguns filtros na aplicação
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']
#podemos definir o que vai aparecer na página administrativa