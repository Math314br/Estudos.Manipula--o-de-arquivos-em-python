#iremos manipular dados para espelhar uma imagen.

# usaremos biblotecas PIL, NUMPY pil para imagens, e numpy para numeros e codigos baixo niviel
from PIL import Image
import numpy as np

def main():
    #carregando imagen original (com o Image.open ele abre imagen e reconhece como imagen)
    img = Image.open("imagenEXEMPLO.jpg")

    # essa função converte a imagen em dados binarios.
    img_data = np.array(img)
    #mostrando os bytes da img
    binario = img_data.tobytes()

    print("\n",img_data.shape,"\n")

    #salvara os dados binarios em um arquivo novo.
    with open("original_foto.bin","wb") as file:
        file.write(binario)
    #criaremos uma copia do arquivo binario.
    with open("original_foto.bin", "rb") as original_arquivo:
        data = original_arquivo.read()
    with open("copia_foto.bin", "wb") as copia_arquivo:
        copia_arquivo.write(data)
    # carregar e mostrar imagen manipulada 
    foto_mod = np.frombuffer(data, dtype=np.uint8).reshape(img_data.shape)

    # inverte todos os bytes fazendo imagen inverter.
    foto_mod = np.fliplr(foto_mod)

    foto_final = Image.fromarray(foto_mod)
    foto_final.show()

    print("FOTO INVERTIDA COM SUCESSO :D")

if __name__ == "__main__":
    main()