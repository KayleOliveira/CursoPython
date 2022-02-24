# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random


tupla = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))


#Usando o max e min eu elimino essas linhas de código
#maior = menor = 0
# while True:
#     for c in range(0, len(tupla)):
#         if c == 0:
#             maior = menor = tupla[0]
#         if c > maior:
#             maior = tupla[c]
#         if c < menor:
#             menor = tupla[c]
#     break               

print(f'Números: {tupla}')
print(f'Maior: {max(tupla)}')
print(f'Menor: {min(tupla)}')