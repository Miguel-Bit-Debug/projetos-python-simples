from random import randint

computador = randint(1, 10)
maior = computador
menor = computador

while True:
    try: 

        usuario = int(input('Tenta adivinhar o número que estou pensando [0 para sair] :'))

        if usuario > maior and usuario > 0:
            print('Um pouco menos')
        
        elif usuario < menor and usuario > 0:
            print('Um pouco mais')
        
        elif usuario == maior and usuario == menor:
            print(f'Acertou usuário: {usuario} ---- computador: {computador}')
            break
        elif usuario == 0:
            print('Até mais :)')
            break

    except KeyboardInterrupt:
        print('você apertou CTRL + C bye!')
        break
    except:
        print('Erro interno')