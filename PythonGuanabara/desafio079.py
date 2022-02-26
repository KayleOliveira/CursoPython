# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro,ele não será adicionado. No final,serão exibidos todos os valores únicos digitados,em ordem crescente.

lista = list()
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Número adicionado com sucesso...')
    else:
        print('Número já existente...')
    choice = ' '
    while choice not in 'SN':
        choice = input('Quer continuar? [S/N]:').strip().upper()[0]
    if choice == 'N':
        break
lista.sort()
print(f'Lista: {lista}')