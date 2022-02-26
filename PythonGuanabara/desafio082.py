# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.


valores = list()
impares = list()
pares = list()

while True:
    num = int(input('Digite um número: '))

    valores.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)    

    choice = ' '
    while choice not in 'SN':
        choice = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if choice in 'N':
        break

impares.sort
pares.sort

print(f'Números: {valores}')
print(f'Ímpares: {impares}')
print(f'Pares: {pares}')