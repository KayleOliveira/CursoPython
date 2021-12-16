# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
# no separadamente

# Ex: Ana Maria de Sousa
# primeiro: Ana
# último: Sousa

nome = input('Nome: ').strip().split()

print(f'Primeiro nome: {nome[0]}\nÚltimo nome: {nome[-1]}')