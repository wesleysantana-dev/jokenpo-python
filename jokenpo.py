from random import randint
from time import sleep
itens = ('pedra' , 'papel' , 'tesoura')
computador = randint(0,2)
print('''SUA ESCOLHA
[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input('Digite sua escolha '))
print('='*40)
print('CARREGANDO...')
sleep(2)
print('o jogador escolheu {}'.format(itens[jogador]))
print('o computador escolheu {}'.format(itens[computador]))
print('='*40)
if jogador == 0:
    if computador == 0:
        print('EMPATE')
    elif computador == 1:
        print('COMPUTADOR VENCE')
    elif computador == 2:
        print('JOGADOR VENCE')
    else:
        print('NUMERO INVALIDO')
elif jogador == 1:
    if computador == 0:
        print('JOGADOR VENCE')
    elif computador == 1:
        print('EMPATE')
    elif computador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('numero invalido')
elif jogador == 2:
    if computador == 0:
        print('COMPUTADOR VENCE')
    elif computador == 1:
        print('JOGADOR VENCE')
    elif computador == 2:
        print('EMPATE')
    else:
        print('numero invalido')
