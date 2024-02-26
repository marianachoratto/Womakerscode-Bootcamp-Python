from django import forms
from cursos.models import Curso

#Como fazer a conexão do formulário com o banco de dados? 
class CursoForm(forms.ModelForm):
    #importar os campos do BD de forma facilitada
    class Meta:
        #A tabela que você quer importar:
        model = Curso
        fields = ['titulo', 'nivel', 'carga_horaria', 'data_do_curso', 'descricao']