# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

mediaAge = 0
oldMan = ''
women = 0


for c in range(0, 4):
    print(f'------ {c+1}° PESSOA ------')
    nome = input('Nome: ').strip().split()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()


