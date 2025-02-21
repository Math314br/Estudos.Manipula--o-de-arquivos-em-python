#iremos movimentar apenas arquivos (pdf,txt,img) para outro diretorio
import os   
import shutil

#vamos cirar  novos diretorios
def criar_diretorios(diretorios):
    for diretorio in diretorios:
        #caso nao exista ele, ele cria:
        if not os.path.exists(diretorio):
            try:
                os.makedirs(diretorio)
                print(f"Novo Diretorio criado")
            except PermissionError:
                print("sem premissão para criar novo diretorio")
            except Exception as erro:
                print(f"Erro inesperado ao criar {diretorio}: {erro}")
#mover arquivos para diretorios
def mover_arquivos(diretorio_origem):
    #esse listdir lista todos arquivos do diretorio 
    for arquivo in os.listdir(diretorio_origem):
        #depois de verifcar direotorio de origem com arquivos etc iremos separar eles em lista dps do  . para pegar arquvios tipo  .txt .jpg etc
        caminho = os.path.join(diretorio_origem,arquivo)
        if os.path.isfile(caminho):
            extensao = arquivo.split('.')[-1].lower()
            #se arquvios no caso na extensao tiver dps do ponto pdf txt ou jpg ele ira mexer o arquivo para diretorio de destino.
            if extensao in ['pdf','txt','jpg']:
                diretorio_destino = os.path.join(diretorio_origem, extensao)
                try:
                    shutil.move(caminho,diretorio_destino)
                    print(f"{arquivo} movido para {diretorio_destino}.")
                except Exception as erro:
                    print(f"Erro inesperado ao mover o {arquivo}: {erro}")
# função  principal
def main():
    diretorio_destino  = "diretorio_destino"
    diretorios = [os.path.join(diretorio_destino,'pdf'),
                  os.path.join(diretorio_destino, 'txt'),
                  os.path.join(diretorio_destino,'jpg')]
    # ira criar diretorios se eles nao existirem.
    criar_diretorios(diretorios)

    # mover arquvios para os diretorios correspodentes
    mover_arquivos(diretorio_destino)

if __name__ == "__main__":
    main()




