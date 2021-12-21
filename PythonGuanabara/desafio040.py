# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO

# – Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO

from math import ceil

nota1 = float(input('Digite sua nota 1: '))
nota2 = float(input('Digite sua nota 2: '))

media = float((nota1 + nota2)/2)

if media < 5:
    print(f'Sua média foi {ceil(media):.1f}')
    print('\033[1;31mREPROVADO!\033[1;31m')
elif media > 5 and media < 7:
    print(f'Sua média foi {ceil(media):.1f}')
    print('\033[1;33mRECUPERAÇÃO!\033[1;33m') 
else:
    print(f'Sua média foi {ceil(media):.1f}')
    print('\033[1;32mAPROVADO!\033[1;32m')
