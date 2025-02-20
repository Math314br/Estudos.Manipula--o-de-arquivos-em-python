#cifra ZENIT POLAR basicamente iremos substituir cada letra da palavras pela outra.
def zenit_polar(text):
    #metodo replace
    recolocar = [ ('z','p'),('e','o'),('n','l'),('i','a'),('t','r'),#letras minusculas
                 ('Z','P'),('E','O'),('N','L'),('I','A'),('T','R')]#LETRAS MAIUSCULA
    #foi feito uma tupla com pares lista, com  função old new, basicamente ele ira substiuir
    #cada par pelo outro que esta dentro de cada elemento.
    for old, new in recolocar:
        text = text.replace(old,new)
    return text
def main():
    frase = "O céu estava claro,E a lua brilha no horizonte."
    frase =  frase.title()#deixa primeira letra de cada palavra  em  maiscula
    
    palavras = frase.split()

    # AQUI IRA USAR CADA PALAVRA NA LISTA USANDO ZENIT POLAR 
    palavras_codficadas = [zenit_polar(palavra) for palavra in palavras]
 
    #aki estara juntando os espaço das palavras codificadas porque elas estao em lista ent estariam separadas porem junta igual antes
    palavras_cod = " ".join(palavras_codficadas)
     # mostrar palavras codificada e nao cod
    print("ORIGINAL: ", frase)
    print("CODIFICADO:", palavras_cod)

if __name__ == '__main__':
    main()