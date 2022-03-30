import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    max_tentativas = 0
    pontos = 100

    print(numero_secreto)
    print("Em qual o nível de dificuldade você quer jogar?")
    print("(1)Fácil (2)Médio (3)Difícil")

    nivel = int(input("Digite o nível:"))

    if(nivel == 1):
        max_tentativas = 10
    elif(nivel == 2):
        max_tentativas = 5
    elif(nivel == 3):
        max_tentativas = 3
    else:
        print("A dificuldade do jogo é entre 1 e 3!")

    for rodada in range(1, max_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, max_tentativas))

        chute_str = input("Digite o seu número: ")
        print ("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print(f"Parabéns você acertou, e fez {pontos} pontos!")
            print("Fim do jogo.")
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if(rodada == max_tentativas):
                    print(f"O número secreto era {numero_secreto}. Voĉe fez {pontos} pontos.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if(rodada == max_tentativas):
                    print(f"O número secreto era {numero_secreto}. Voĉe fez {pontos} pontos.")
                    
if(__name__ == "__main__"):
    jogar()