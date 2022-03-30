import forca
import adivinhacao_for

def escohlha():
    print("*********************************")
    print("********Escolha seu jogo*********")
    print("*********************************")

    print("(1)Forca (2)Adivinhação")

    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    if(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao_for.jogar()

if(__name__ == "__main__"):
    escohlha()