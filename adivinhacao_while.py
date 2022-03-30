print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
max_tentativas = 3
rodada = 1

while(rodada <= max_tentativas):
    print("Tentativa {} de {}".format(rodada, max_tentativas))
    chute_str = input("Digite o seu número: ")
    print ("Você digitou", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Parabéns você acertou!")
        print("Fim do jogo.")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

    rodada = rodada + 1

    print("Fim do jogo.")