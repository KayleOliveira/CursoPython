# Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar

# [ 2 ] multiplicar

# [ 3 ] maior

# [ 4 ] novos números

# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))
print('''==================
[ 1 ] SOMAR

[ 2 ] MULTIPLICAR

[ 3 ] MAIOR

[ 4 ] NOVOS NÚMEROS

[ 5 ] SAIR
==================''')
choice = int(input('Selecione uma opção: '))

while choice != 5:
    if choice > 5:
        choice = int(input('Opção Inválida!Tente novamente : '))
    if choice == 1:
        print(f'Soma: {n1 + n2}')
        sleep(1)
        print('''
==================
[ 1 ] SOMAR

[ 2 ] MULTIPLICAR

[ 3 ] MAIOR

[ 4 ] NOVOS NÚMEROS

[ 5 ] SAIR
==================''')
        choice = int(input('Selecione uma opção: '))
    if choice == 2:
        print(f'Multiplicação: {n1 * n2}')
        sleep(1)
        print('''
==================
[ 1 ] SOMAR

[ 2 ] MULTIPLICAR

[ 3 ] MAIOR

[ 4 ] NOVOS NÚMEROS

[ 5 ] SAIR
==================''')
        choice = int(input('Selecione uma opção: '))
    if choice == 3:
        if n1 > n2:
            print(f'Maior: {n1}')
        else:
            print(f'Manor: {n2}')
        sleep(1)
        print('''
==================
[ 1 ] SOMAR

[ 2 ] MULTIPLICAR

[ 3 ] MAIOR

[ 4 ] NOVOS NÚMEROS

[ 5 ] SAIR
==================''')
        choice = int(input('Selecione uma opção: '))    
    if choice == 4:
        n1 = float(input('Informe o primeiro valor: '))
        n2 = float(input('Informe o segundo valor: '))
        print('''
==================
[ 1 ] SOMAR

[ 2 ] MULTIPLICAR

[ 3 ] MAIOR

[ 4 ] NOVOS NÚMEROS

[ 5 ] SAIR
==================''')
        choice = int(input('Selecione uma opção: '))