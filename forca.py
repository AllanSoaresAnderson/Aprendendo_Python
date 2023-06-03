
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    print("Fim do jogo")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    print(letras_acertadas)
    acertou = False
    enforcou = False

    while (not acertou and not enforcou):
        chute = input("Digite uma letra: ").strip()
        index =0
        for letra in palavra_secreta:
            if (chute.lower() == letra.lower()):
                letras_acertadas[index] = chute.lower()
            index = index + 1
        print (letras_acertadas)


if __name__ == "__main__":
    jogar()