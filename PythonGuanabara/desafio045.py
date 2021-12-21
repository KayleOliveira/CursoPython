# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ['PEDRA', 'PAPEL', 'TESOURA']
computer = randint(0, 2)

print("""Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

player = int(input('Qual a sua jogada? '))

if player > 2:
    print('Jogada inválida')
else:
    print('\nJO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!\n')
    sleep(0.5)  

    print(f'Computador: {itens[computer]}')
    print(f'Player: {itens[player]}')

    if computer == player:
        print('\n\033[1;33mDRAW\033[1;33m')
    elif computer == 0 and player == 2:
        print('\n\033[1;32mCOMPUTER WINS\033[1;32m') 
    elif computer == 1 and player == 0:
        print('\n\033[1;32mCOMPUTER WINS\033[1;32m') 
    elif computer == 2 and player == 1:
        print('\n\033[1;32mCOMPUTER WINS\033[1;32m') 
    else:
        print('\n\033[1;32mPLAYER WINS\033[1;32m')
