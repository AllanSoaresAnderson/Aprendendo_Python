
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    print("Fim do jogo")

    palavra_secreta = "banana"
    acertou = False
    enforcou = False

    while (not acertou and not enforcou):
        chute = input("Digite uma letra: ").strip()

        index =0
        for letra in palavra_secreta:

            if (chute.lower() == letra.lower()):
                print ("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print ("jogando")


if __name__ == "__main__":
    jogar()