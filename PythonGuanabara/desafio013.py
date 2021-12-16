# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de desconto

n = float(input('Digite o salário atual do funcionário: R$'))
por = float(input('Digite o valor da porcentagem do aumento: '))

print(f'O salário final do funcionário com o aumento é: R${n+(n*por/100):.2f}')

