# Desenvolva um programa que leia as duas notas de um aluno, e calcule sua média

nota1 = float(input('Digite sua nota 1: '))
nota2 = float(input('Digite sua nota 2: '))

media = float((nota1 + nota2)/2)

if media >= 7:
    print(f'Sua média é {media}, portanto está aprovado!')
else:
    print(f'Sua média é {media}, portanto está reprovado!')
