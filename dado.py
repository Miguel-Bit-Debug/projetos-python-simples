from random import randint

while True:
    try:
        num = int(input("Digite o número que você acha que vai ser sorteado [0 para sair]: "))
        dado = randint(1, 6)

        if num == dado:
            print(f'\n\nVocê acertou! jogador: {num} ---- computador: {dado} \n\n')

        elif num != dado and num > 0 and num <= 6:
            print(f'\n\nVocê errou! jogador: {num} ---- computador: {dado} \n\n')
        
        elif num > 6:
            print('\n\nErro! Digite números de 1 á 6\n\n')

        elif num == 0:
            break
        
    except KeyboardInterrupt:
        print('você apertou CTRL + C bye!')
        break

    except:
        print('Erro interno')
        