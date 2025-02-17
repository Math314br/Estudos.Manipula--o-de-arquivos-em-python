#importamos biblioteca do sistem
import os

#irei criar um arquivo que nao existe ainda usando o 'w', como arquivo nao existe ainda
#se eu usar o open direto ele nao iria abrir e daria erro.
# usando o encoding='utf-8' é bom porque formata meu codigo corretamente sem erros de caracteres
arquivo1 = open("dados1.txt",'w', encoding='utf-8')
#esse print os.path.abspath  mostra o local do arquivo aonde foi criado
print(os.path.abspath(arquivo1.name))
#write escreve no arquivo.
arquivo1.write("Testando a escrita com write\n")
# quebrando linha com \n
arquivo1.write("Testando segunda linha\n")

# close fecha o arquivo. 
arquivo1.close()

#esse print ira exibir no meu painel os detalhes do arquivo 1.
print (f"Detalhes Do Arquivo aberto: {arquivo1}")

# EXIBINDO OS ATRIBUTOS DO ARQUIVOS  COM FUNÇÃO NAME,MODE,CLOSED
print("Nome Do Arquivo: ", arquivo1.name)
print("Modo Que Arquivo Foi Aberto: ", arquivo1.mode)
print("Verificando Se Arquivo Esta Fechado: ", arquivo1.closed)

# EXIBIR CAMINHO RELATIVO E ABSOLUTO
relpath = os.path.relpath('dados1.txt')
abspath = os.path.abspath('dados1.txt')

#print que ira mostrar caminhos
print('Caminho Relativo:', relpath)
print('Caminho absoluto:', abspath)

# iremos abrir novamente o arquivo para add um final com "A" e abriremos com with, porque ele fecha automaticamente

with open("dados1.txt", 'a') as arquivo1:
 arquivo1.write("FIM DO ARQUIVO\n")
 print ("arquivo foi finalizado")
 

