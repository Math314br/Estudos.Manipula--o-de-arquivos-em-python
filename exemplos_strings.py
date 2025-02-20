from datetime import datetime
#contador de linhas
with open("frases.txt",encoding='utf-8') as  arquivo:
    contador = 0
    print("Representação das linhas:")
    for linha in arquivo:
        #usando o strip para caso tenha quebra linhas ou linhas vazia assim ele nao conta elas.
        linha_limpa =  linha.strip()
        print(repr(linha_limpa))
        if linha_limpa:
            contador += 1
    print(f"Total de linnhas: {contador}")
#contar letras
with open('frases.txt', encoding='utf-8') as letras:
    texto = letras.read()
    #aki usei o LOWER para convertei texto para minuscula assim é melhor para contar caso tenha maiscula junto

    contado = texto.lower().count("a")
    print(f'total de letras A: {contado}')
#separando as palavras 
frase1 = "Acordar cedo todo dia é chato"
frase2 = "jose moura lima do santos"
frase3 = "carro,moto,caminhao,barco"

#slipt separa dps do espaço em lista separando os elementos. slipt tambem pode receber um argumento tipo SEPARE DPS DA VIRGULA ou do  ponto

lista  = frase1.split()
print(f"Palavras separadas:{lista}")
lista2 = frase2.split()
print(lista2)
lista3 = frase3.split(",")
print(lista3)

#precisão numerica
valor = 3.14159
print (f"Valor de Pi com 2 casas decimais: {valor:.2f}")
# data formatada
hoje = datetime.now()
dataFormatada = f"Data: {hoje:%d/%m/%y}"
print(dataFormatada)
