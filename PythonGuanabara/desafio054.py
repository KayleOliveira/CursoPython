# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0

for c in range(0 , 7):
    ano = int(input(f'Informe o ano de nascimento da {c+1}° pessoa: '))
    age = date.today().year - ano
    if age >= 21:
        maior += 1
    else:
        menor += 1    

print(f'\n{maior} pessoas ainda são de maiores e\n{menor} pessoas são de menor')