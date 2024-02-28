from django import forms
from cursos.models import Curso
from datetime import date

#Como fazer a conexão do formulário com o banco de dados? 
class CursoForm(forms.ModelForm):
    #fazer uma validação extra. Impedir cadastros em datas passadas
    #clean_nome_da_variavel
    def clean_data_do_curso(self):
        data_do_curso = self.cleaned_data['data_do_curso']
        hoje = date.today()
        if data_do_curso < hoje:
            raise forms.ValidationError('Não é possível cadastrar um curso no passado.')
        return data_do_curso

    #importar os campos do BD de forma facilitada
    class Meta:
        #A tabela que você quer importar:
        model = Curso
        fields = ['titulo', 'nivel', 'carga_horaria', 'data_do_curso', 'descricao']