# Crie um programa  que leia um número real qualquer pelo teclado e mostre sua porção inteira 
# ex (6.123 == 6)

import math
num = float(input('Digite um número: '))
print(f'Número inteiro: {math.floor(num)}')