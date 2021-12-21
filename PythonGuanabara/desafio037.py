# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
base = int(input("""Informe a base de conversão.\n
1. Binário\n
2. Octal\n
3. Hexadecimal\n
: """))

if base == 1:
    print(f'Binário: {bin(num)[2:]}')
elif base == 2:
    print(f'Octal: {oct(num)[2:]}')
elif base == 3:
    print(f'Hexadecimal: {hex(num)[2:]}')
else:
    print('Opção Inválida!')
        