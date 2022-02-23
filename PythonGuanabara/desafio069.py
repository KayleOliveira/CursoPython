# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

mais18 = homens = mMenos20 = 0

while True:
    print('CADASTRE UMA PESSOA')

    idade = int(input('Idade: '))
    while idade < 0:
        idade = int(input('Idade: '))
    if idade > 18:
        mais18 += 1
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mMenos20 += 1
    choice = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while choice not in 'SN':
        choice = input('Quer continuar? [S/N]: ').strip().upper()[0]
    
    if choice == 'N':
        break

print(f'Maiores de 18 anos: {mais18}')
print(f'Total de homens: {homens}')
print(f'Mulheres com menos de 20 anos: {mMenos20}')