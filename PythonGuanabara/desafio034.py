# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do aumento.
# Para salários superiores a R$1250.00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o salário do funcionário: '))

if salario > 1250:
    print(f'O novo salário do funcionário: {salario + (salario * 10 / 100)}')
else:
    print(f'O novo salário do funcionário: {salario + (salario * 15 / 100)}')