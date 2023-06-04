import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")


    arquivo = open("palavras.txt", "r")
    lista_palavras = [palavra.lower().strip() for palavra in arquivo]
    palavra_secreta = lista_palavras[random.randrange(0,len(lista_palavras))]
    letras_acertadas = ["_" for caracter in palavra_secreta]
    print(letras_acertadas)
    acertou = False
    enforcou = False
    erros = 0

    while (not acertou and not enforcou):
        chute = input("Digite uma letra: ").strip().lower()
        index =0
        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute.lower() == letra.lower()):
                    letras_acertadas[index] = chute.lower()
                index = index + 1
            if ("_" not in letras_acertadas):
                acertou = "_" not in letras_acertadas
                print("Você acertou a palavra!!!\nA palavra era:\n {}".format(letras_acertadas))
                break
        else:
            erros = erros + 1
            if (erros ==6):
                print("Putz! Você foi enforcado, o jogo acabou :C")
                enforcou = erros == 6
                break
        print (letras_acertadas)
    print ("Fim do jogo!!!")

if __name__ == "__main__":
    jogar()