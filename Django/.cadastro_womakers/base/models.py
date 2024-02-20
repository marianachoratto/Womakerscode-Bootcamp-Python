from django.db import models

# Criando uma tabela chamada cadastros com os campos nome, email, senha e data
#ATENÇÃO! Não colocar ID, o django cria automaticamente
#ATENÇÃO 2! É SEM VÍRGULA! 
class Cadastro(models.Model):
    nome= models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, default='default@email.com')
    senha = models.CharField(max_length=50, default='12345')
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.nome} [{self.email}]'
#com isso nosso modelo vai saber o que apresentar quando ele ser convertido para texto
    #classe meta indica meta informações
    class Meta:
        verbose_name = 'Formulário de contato'
        verbose_name_plural = 'Formulários de contatos'
        ordering = ['-data'] #toda a consulta vai ser definida por data. o - indica decrescente 
