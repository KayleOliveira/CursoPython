# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for c in range(0, 5):
    peso = float(input(f'{c+1}° Peso(kg): '))
    if peso > maior:
        maior = peso
    elif menor == 0:
        menor = peso
    elif peso < menor:
        menor = peso


print(f'Maior peso: {maior}Kg')
print(f'Menor peso: {menor}Kg')    