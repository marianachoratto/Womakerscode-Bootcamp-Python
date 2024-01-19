'''def soma():
    numero1 = int(input('Digite um numero:'))
    numero2= int(input('Digite outro numero:'))
    print(numero1 + numero2)
    subtracao()

def subtracao():
    # calculo = 10+2
    # print(calculo)
    numero1 = int(input('Digite um numero:'))
    numero2= int(input('Digite outro numero:'))
    print(numero1 - numero2)

soma()'''

# Uma função que define argumentos pode ser chamada sem argumentos?
# Sim, uma função que define argumentos pode ser chamada sem argumentos, desde que todos os argumentos sejam definidos com valores padrão (ou seja, eles têm um valor que será usado 
# se nenhum argumento correspondente for fornecido na chamada da função).

# def minha_funcao(arg1="valor padrão", arg2=None):
#    print(arg1, arg2)

# Nesta função, arg1tem um valor padrão de "valor padrão"e arg2tem um valor padrão de None. Portanto, você pode chamar esta função sem fornecer nenhum argumento


#MANIPULAÇAO DE ARQUIVOS

#Nos temos 3 processos quando estamos manipulando arquivos em python: abertura, escrita e leitura
#ABERTURA
# temos 2 formas de abertura: (1)somente para leitura, (2)escrita
    #arquivo_leitura= open(file, "r")
    #arquivo_escrita = open(file, 'w')


def multiplicacao():
    #definindo um arquivo 
    file= 'arquivo.txt'

    #ESCRITA
    #arquivo para escrita
    #1- abre o arquivo
    arquivo_escrita = open(file, 'w') #w de write 
    #2- escreve
    arquivo_escrita.write('texto a ser escrito')
    #3- fecha
    arquivo_escrita.close()

    #LEITURA
    #Um arquvivo escrito não dá para ler, devemos abrir um arquivo de somente leitura
    #1- Primeiro abre um arquivo para leitura
    arquivo_leitura= open(file, "r") #r de read.
    #2- lê
    leitura = arquivo_leitura.read()
    print(leitura) #o que essa variavel está salvando?
    #3- fecha
    arquivo_leitura.close()
    
    #abertura de arquivos binários
    arquivo_binario = open(file, 'wb') #write-binary

#manipulacao de arquivos serve muito com dados, que você quer salvar centanas de dados de forma automatizada

#open(caminhoDoArquivo, modoDeAbertura)
    
    #Modos de abertura
    #r = read
    #a = append = adiciona no arquivo já existente
    #w = write = apaga tudo e começa a escrever de novo
    #x = criar arquivo
    #r+ = leitura e escrita

#ATENCAO! NAO ESQUECER DE FECHAR O ARQUIVO. ELE ABERTO GASTA MEMÓRIA
    
#Funcão para ver se o arquivo pode ser lido 
#   f = open("demofile.txt", "r")
    # print(arquivo.readable)# This will output: True 
# Ele retorna Truese o arquivo for aberto em um modo que permita a leitura e Falsecaso contrário. 
    

#arquivo.readline() >> lê a 1 linha do arquivo 
#arquivo.readlines() >> retorna uma lista do conteúdo
    
multiplicacao()