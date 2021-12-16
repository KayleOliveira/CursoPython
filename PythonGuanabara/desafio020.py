# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteado

from random import shuffle, choices

aluno1 = input('Aluno1: ')
aluno2 = input('Aluno2: ')
aluno3 = input('Aluno3: ')
aluno4 = input('Aluno4: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print(f'Ordem: {alunos}')
print(f'valor: {choices(alunos, k=4)}')