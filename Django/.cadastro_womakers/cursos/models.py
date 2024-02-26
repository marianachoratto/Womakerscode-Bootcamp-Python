from django.db import models

# Create your models here.

class Curso(models.Model):
    # Como colocar escolhas específicas nos campos?
    niveis_de_curso = (
        #As tuplas são compostas (oQueSalva, OqueAparece)
        ('Iniciante', 'Iniciante'),
        ('Intermediário', 'Intermediário'),
        ('avançado', 'avançado')
    )
    titulo= models.CharField(max_length=50)
    nivel= models.CharField(max_length=50, choices= niveis_de_curso)
    carga_horaria= models.IntegerField()
    #IntegerField não precisa de max_lenght
    #help text
    data_do_curso= models.DateField(help_text='aaaa/mm/dd')
    descricao= models.TextField()

    #Para a parte administrativa:
    def __str__(self):
        return f'{self.titulo}: {self.data_do_curso} - {self.carga_horaria}'
    
    #classe meta indica metadados. Ele vai trocar o nome dos campos na classe administrativa
    class Meta:
        verbose_name = 'Cadastro de Curso'
        verbose_name_plural = 'Cadastros de Curso'
        #o - indica ordem decrescente
        ordering = ['-data_do_curso']