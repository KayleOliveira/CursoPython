# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome dos alunos e escrevendo o nome do escolhido na tela

import random

aluno1 = input('Aluno1: ')
aluno2 = input('Aluno2: ')
aluno3 = input('Aluno3: ')
aluno4 = input('Aluno4: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

print(f'Aluno escolhido: {random.choice(alunos)}')