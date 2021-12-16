# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60.00/dia e R$0.15/Km rodado

dias = float(input('Informe a quantidade de dias alugados: '))
km = float(input('Informe a quantidade de km rodados: '))
print(f'O valor a pagar é: R${(60 * dias) + (km * 0.15):.2f}')