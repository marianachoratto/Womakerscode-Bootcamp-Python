#A classe logável é responsável por escrever tudo o que você faz com o programa no seu computador. Se algo der errado, você tem um relatório de como tudo foi usado.
#Essa classe tira a responsabilidade do programador de escrever essa classe de log, o programador só escreve as mensagens que vão aparecer e não precisa se preocupar com a escrita do arquivo. 

'''A classe Logavel define o método logar. Qualquer classe que herdar dela vai conseguir escrever uma mensagem no log e nós vamos saber de onde a mensagem está vindo pelo atributo nome_da_classe que é inicializado no construtor.'''
class Logavel:
    def __init__(self):
        self.nome_da_classe = ''

    def logar(self, mensagem):
        print('Mensagem da classe ' + self.nome_da_classe + ': ' + mensagem)

'''A classe Conexao serve para conectar a um servidor de banco de dados. O servidor costuma ser um endereço de IP com uma porta.'''
class Conexao: #numero IP 
    def __init__(self):
        self.servidor = ''

    def conectar(self):
        print('Conectando ao banco de dados no servidor ' + self.servidor)
        # Lógica para realizar a conexão aqui

'''A classe MySqlDatabase é uma classe de exemplo que se conecta ao banco de dados MySql, que herda tanto de conexão quanto de logável.'''
class MySqlDatabase(Conexao, Logavel):
    def __init__(self):
        super().__init__()
        self.nome_da_classe = 'MySqlDatabase'
        self.servidor = 'MeuServidor'

'''O meu framework super chique aqui é só um metódo que recebe um objeto chamado item e testa se esse objeto é uma instância de cada uma das classes. Ele só chama os métodos pertinentes se for.'''
def framework(objeto):
    if isinstance(objeto, Conexao):
        objeto.conectar()
    if isinstance(objeto, Logavel):
        mensagem = 'Olá mulheres maravilhosas do Bootcamp de Python.'
        objeto.logar(mensagem)

conexao_mysql = MySqlDatabase()
framework(conexao_mysql)