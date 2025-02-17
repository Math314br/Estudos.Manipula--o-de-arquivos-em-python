# manipulando arquivos de textos.

#função principal
def main():
    # aqui ira pegar entradas do usuario e add a uma lista e ao escrever sair, para o input
    print("DIGITE SUAS FRASES, DIGITE 'sair' PARA SALVAR O ARQUIVO")
    frases = []
    #quanto for verdadeiro a entrada continua add o input 
    while True:
        entrada = input("> ")
        if entrada.lower() ==  "sair":
            break
        # add as frases a frases lista.
        frases.append(entrada)
    #cria um arquivo novo de texto com frases. quebrando linhas.
    with open("frases.txt","w") as arquivo:
     for frase in frases:
        arquivo.write(frase+"\n")
    # irei modificar as entradas do input  (as frases)

    print("Arquivo Original Criado")
    frases_mod = []
    with open("frases.txt", "r") as arquivo:
        for linha in arquivo:
            #STRIP DA ESPAÇOS. E UPPER DEIXA TUDO MAIUSCULO. ISSO ADD NA LISTA FRASES_MOD
            frases_mod.append(linha.strip().upper())
    # agora irei rescrever meu arquivo texto original porem com as modificações.
    with open("frases.txt","w",encoding='utf-8') as arquivo:
        for linha in frases_mod:
            arquivo.write(linha + "\n")
        print   ("TODAS AS FRASES ESTÃO EM MAIUSCULAS AGORA")
# aki inicia a função main
if __name__ == "__main__":
    main()


