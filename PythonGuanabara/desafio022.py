# Crie um programa que leia o nome completo de uma pessoa e mostre:

# + O nome com todas as letras maiúsculas 
# + O nome com todas as letras minúsculas
# + Quantas letras ao todo (sem considerar espaços)
# + Quantas letras tem o primeiro nome

nome = input('Nome completo: ')

print(f'\nMaiúsculo: {nome.upper()}')
print(f'Minúsculo: {nome.lower()}')
nome = nome.replace(' ', '')
print(f'Tamanho do nome: {len(nome)}')
nomeS = nome.split()
print(f'Qtd letras primeiro nome: {len(nomeS[0])}')


# nome = input('Nome completo: ').split()
# print(f'\nMaiúsculo: {nome.upper()}')
# print(f'Minúsculo: {nome.lower()}')
# print(f'Tamanho do nome: {len(nome) - nome.count(" ")}')
# print(f'Qtd letras primeiro nome: {len(nome[0])}')