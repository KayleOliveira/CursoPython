# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('BANCO LILO NARA')

# tot50 = tot10 = tot20 = 0

# while True:
#     valor = int(input('Quanto deseja sacar? R$'))
#     if valor >= 50:
#         tot50 = int(valor / 50)
#         valor = valor % 50

#     if valor >= 20:
#         tot20 = int(valor / 20)
#         valor = valor % 20    
    
#     if valor >= 10:
#         tot10 = int(valor / 10)
#         valor = valor % 10
    
#     valor == 0
#     break

# print(f'Cédulas de R$50: {tot50}')
# print(f'Cédulas de R$20: {tot20}')
# print(f'Cédulas de R$10: {tot10}')
# print(f'Cédulas de R$1: {valor}')

nota = 50
totnotas = 0
valor = int(input('Quanto deseja sacar? R$'))

while True:
    if valor >= nota:
        valor -= nota
        totnotas += 1
    else:
        if totnotas > 0:
            print(f'{totnotas} Cédulas de R${nota:.2f}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totnotas = 0
        if valor == 0:
            break    