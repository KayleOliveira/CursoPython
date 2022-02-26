# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

import turtle


valores = []

maior = menor = 0

for count in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {count}: ')))
    if count == 0:
        maior = menor = valores[count]
    else:
        if valores[count] > maior:
            maior = valores[count]
        if valores[count] < menor:
            menor = valores[count]

print(f'Voçê digitou os valores {valores}')


print(f'Menor: {menor} na posição ', end=' ')
for index, valor in enumerate(valores):
    if valor == menor:
        print(f'{index}...')
print(f'Maior: {maior} na posição ', end=' ')
for index, valor in enumerate(valores):
    if valor == maior:
        print(f'{index}...')