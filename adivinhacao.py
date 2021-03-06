import random
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000
    #print(numero_secreto)

    print('Escolha o nível de dificuldade entre 1 e 3:')
    print('(1) Fácil (2) Médio (3) Difícil\n')
    nivel = int(input('Defina o nível: '))

    while(nivel < 1 or nivel > 3):
        print('Escolha o nível de dificuldade entre 1 e 3:')
        nivel = int(input('Defina o nível: '))
        continue
    if(nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while (rodada <= total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        rodada = rodada + 1
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute <1 or chute >100):
            if(rodada<total_de_tentativas):
                print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou e fez {} pontos!" .format(pontos))
            print("Fim do jogo")
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    if(chute != numero_secreto):
        print("O número secreto era:", numero_secreto)
        print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()