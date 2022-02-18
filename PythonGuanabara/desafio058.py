# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
import time
num = random.randint(0, 10)


print('Acabei de pensar em um valor de 0 à 10, tente adivinhá-lo!')
palpite = int(input('Tente acertar o valor: '))
tentativas = 1
print('Processando...')
time.sleep(1)

while palpite != num:
    if palpite < num:
        palpite = int(input('Mais... Tente outra vez: '))
        tentativas += 1
    else:
        palpite = int(input('Menos... Tente outra vez: '))
        tentativas += 1
    

print(f'PLAYER WINS! {tentativas} tentativas')
