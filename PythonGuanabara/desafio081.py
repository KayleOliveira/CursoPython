# Crie um programa que vai ler vários números e colocar em uma lista,
# Depois disso, mostre:

# A) Quantos números foram digitados.

# B) A lista de valores, ordenada de forma decrescente.

# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()

while True:
    lista.append(int(input('Digite um número: ')))

    choice = ' '
    while choice not in 'SN':
        choice = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if choice in 'N':
        break

print(f'Números digitados: {len(lista)}')
lista.sort(reverse=True)
print(f'Lista ordenada: {lista}')

if 5 in lista:
    print('O valor 5 foi encontrado na lista')
else:
    print('O valor 5 não foi encontrado na lista')