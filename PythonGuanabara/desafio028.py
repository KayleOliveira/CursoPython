# Escreva um programa que faça o computador 'pensar' em número inteiro entre 0 e 5 e peça para
# o usúario tentar descobrir qual foi o número escolhido pelo computador

# O programa deverá escrever na tela se o usúario venceu ou perdeu

import random
import time
num = random.randint(0, 5)

palpite = int(input('Tente acertar o valor: '))
print('Processando...')
time.sleep(1)

if palpite == num:
    print(f'A resposta era {num}')
    print(f'Seu palpite {palpite} está correto, voçê venceu!')
else:
    print(f'A resposta era {num}')
    print(f'Seu palpite {palpite} está incorreto, vitória do computador')    