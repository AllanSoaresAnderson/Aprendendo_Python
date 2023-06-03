import advinhacao
import forca


def iniciar():
    print("*********************************")
    print("********Jogos em Python!*********")
    print("*********************************")

    print("Qual jogo você quer jogar?")
    print("(1) Advinhação (2) Forca")
    escolha = int(input("Digite qual jogo você quer jogar: "))

    if escolha == 1:
        print("Começando o jogo de adivinhação [...]")
        advinhacao.jogar()
    else:
        print("Começando o jogo de forca [...]")
        forca.jogar()


if __name__ == "__main__":
    iniciar()
