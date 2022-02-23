# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

print('VAMOS JOGAR PAR OU ÍMPAR!')
vitorias = 0

while True:
    computador = random.randint(0, 10)
    num = int(input('Digite um valor de 0 à 10: '))
    while num > 10:
        num = int(input('Inválido, Digite um valor de 0 à 10: '))
    choice = input('Par ou Ímpar? [P/I]: ').strip().upper()[0]
    while choice != 'P' and choice != 'I':
        choice = input('Inválido, Par ou Ímpar? [P/I]: ').strip().upper()[0]
    soma = num + computador
    print(f'Você jogou {num}, e o computador jogou {computador}. Total de {soma},', end=' ')
    print('PAR' if soma % 2 == 0 else 'ÍMPAR')

    if soma % 2:
        resultado = 'P'
    else:
        resultado = 'I'

    if resultado == choice:
        print('Player WINS, Parabéns')
        vitorias += 1
    else:
        print('Computador WINS, GAME OVER')
        break

print(f'Vitórias: {vitorias}')