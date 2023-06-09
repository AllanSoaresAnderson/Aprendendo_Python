import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    print("Defina a dificuldade do jogo:")
    print("(1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input("Digite de 1 a 3: "))
    total_de_tentativas = 0
    pontos = 1000

    if (dificuldade == 1):
        total_de_tentativas = 20
    elif (dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    numero_secreto = random.randrange(1,101)
    rodada = 1

    for rodada in range (1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número de 1 a 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print ("Número inválido, favor digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
        pontos_perdidos = abs(numero_secreto -chute)
        pontos = pontos - pontos_perdidos

    print("Fim do jogo")
    print("A sua pontuação foi de: ", pontos)

#Loop While +++++++++++++++++++++++++++++++++++++++++++

# while (rodada <= total_de_tentativas):
#     print("Tentativa {} de {}".format(rodada,total_de_tentativas))
#     chute_str = input("Digite o seu número: ")
#     print("Você digitou: ", chute_str)
#     chute = int(chute_str)
#
#     acertou = numero_secreto == chute
#     maior = chute > numero_secreto
#     menor = chute < numero_secreto
#
#     if (acertou):
#         print("Você acertou!")
#     else:
#         if (maior):
#             print("Você errou! O seu chute foi maior que o número secreto.")
#         elif (menor):
#             print("Você errou! O seu chute foi menor que o número secreto.")
#
#     rodada = rodada + 1



if __name__ == "__main__":
    jogar()