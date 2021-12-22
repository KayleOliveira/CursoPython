# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
mult = 0

for c in range(1, num + 1):
    if (num % c) == 0:
        print('\033[32m', end='')
        mult += 1
    else:
        print('\033[31m', end='')    
    print(f'{c} ', end='')

print(f'\nO número {num} foi dividido {mult}x')

if mult == 2:
    print('É primo')
else:
    print('Não é primo')    
