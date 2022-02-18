# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaAge = 0
mediaAge = 0
maioridadehomem = 0
nomevelho = ''
totwomen = 0


for p in range(0, 4):
    print(f'------ {p+1}° PESSOA ------')
    nome = input('Nome: ').strip().split()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    somaAge += idade
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totwomen += 1      


mediaAge = somaAge / 4

print(f'Média de idade: {mediaAge}')
print(f'Homem mais velho: {nomevelho} com {maioridadehomem} anos')
print(f'Mulheres com menos de 20 anos: {totwomen}')