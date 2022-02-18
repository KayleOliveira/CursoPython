# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120

import math

num = int(input('Informe um número: '))
count = num
print(f'{num}!=', end=' ')
while count <= num and count >= 1:
    print(count, end='x')
    count -= 1
    if count == 1:
        print(count,'=', math.factorial(num))
        count = 0