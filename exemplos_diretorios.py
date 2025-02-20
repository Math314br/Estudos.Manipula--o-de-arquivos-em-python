import os
#criar um diretorio
try:
  #os.rmdir("pasta") isso aqui removeria o diretorio.
  #cria diretorio
  os.makedirs("pasta")
  print("diretorio criado")
except FileExistsError as erro:
  print("Diretorio ja existe")
  print("Descrição", erro)

#diretorio ja criado com sucesso agora scanear coisas que tem dentro dele.
try:
  entrada = os.scandir("pasta")

  for obj in entrada:
    print(obj)
    print("Nome:", obj.name)
    print("Caminho do diretorio:",obj.path)
    print("é um diretorio?",obj.is_dir())
    print("é um arquivo?",obj.is_file())

except FileNotFoundError:
  print("O diretorio nao foi encontrado")
except NotADirectoryError:
  print("Não é um diretorio.")

