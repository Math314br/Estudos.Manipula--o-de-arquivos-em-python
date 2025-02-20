import os
#ao usar o Exception nos digamos ao python oque fazer quando tiver um erro podemos mandar um comando
#se não o programa fecha 
#exemplos detelhados de se tiver uma exceção oque o programa ira fazer.
print('iniciando o programa')
try:
    open("testenaoexiste.txt", 'r')
    print("Arquivo Aberto!")
except FileNotFoundError as erro:
    print("Arquivo não foi encontrado")
    print('Descrição:',erro)
print('Abrindo outro arquivo')
# aqui seria tratado erro caso nao tivesse permissao para abrir o arquivo:

#try:
    #open("naotempermissao.txt", 'r')
    #print("Arquivo Aberto!")
#except PermissionError as erro:
    #print("Voce não tem permissao para isso")
    #print('Descrição:',erro)

try:
    open("frases.txt", 'x')
    print("Arquivo Aberto!")
except FileExistsError as erro:
    print("Arquivo JA EXISTE!!!")
    print('Descrição:',erro)
# com isso todo erro que der o programa continua rodando porem da um aviso ao usuario.

# tratando execeçoes de REMOVER ARQUIVO E RENOMEAR ARQUIVO
print("TENTANDO REMOVER O ARQUIVO:")
try:
    os.remove("remover.txt")
    print('REMOVENDO O ARQUIVO!!!')
except FileNotFoundError as erro:
    print("arquivo não existe")
    print('Descrição:',erro)
except PermissionError as erro:
    print("Voce não tem permissao para isso")
    print('Descrição:',erro)
except IsADirectoryError as erro:
    print("tentamos remover um diretório usando a função remove, em vez de rmdir.")
    print('Descrição:',erro)
print ('TENTANDO RENOMEAR O ARQUIVO:')
# RENOMEAR O ARQUIVO.
try:
    os.rename("VELHOARQUIVO.txt", "NOVOARQUIVO.txt")
    print("Renomeando O arquivo")
except FileNotFoundError as erro:
    print("arquivo não existe")
    print('Descrição:',erro)
except PermissionError as erro:
    print("Voce não tem permissao para isso")
    print('Descrição:',erro)
except FileExistsError as erro:
    print("Arquivo JA EXISTE!!!")
    print('Descrição:',erro)




