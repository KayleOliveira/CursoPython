# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = maior = menor = 0
count = 1
num = int(input('Digite um número: '))
choice = input('Quer continuar? [S/N]: ').strip().upper()[0]
soma = num

while choice == 'S':
    if count == 1:
        maior = menor = num
    num = int(input('Digite um número: '))
    count += 1
    soma += num
    media = soma / count
    if num > maior:
        maior = num 
    if num < menor:
        menor = num
    choice = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while choice != 'S' and choice != 'N':
        choice = input('Opção Inválida! Quer continuar? [S/N]: ').strip().upper()[0]

print(f'Soma: {soma}')
print(f'Números: {count}')
print(f'Média: {media}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')