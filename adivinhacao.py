import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("Qual nível de dificudade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível:"))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero: ")
        print("Você digitou:", chute_str)
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("*PARABÉNS*Você Acertou!!! E fez {} ".format(pontos))
            break
        else:
            pontos_perdidios = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidios
            if maior:
                print("Você errou !!! Seu chute foi maior que o esperado")
                if rodada == total_de_tentativas:
                    print("O numero secreto era:{} , você fez {}".format(numero_secreto, pontos))
            elif menor:
                print("Você errou !!! Seu chute foi menor que o esperado")
                if rodada == total_de_tentativas:
                    print("O numero secreto era:{} , você fez {}".format(numero_secreto, pontos))
    print("FIM DE JOGO")
