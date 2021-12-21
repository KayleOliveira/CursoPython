# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros

valor = float(input('Informe o valor do produto: R$'))
pagamento = int(input("""Selecione a forma de pagamento: \n
1. À vista (dinheiro/cheque): 10% OFF
2. À vista no cartão: 5% OFF
3. Em até 2x no cartão (sem juros)
4. 3x ou mais no cartão: 20% juros \n
Opção: """))

if pagamento == 1:
    print(f'Valor final: \033[1;32mR${valor - (valor * 10 / 100):.2f}\033[1;32m')
elif pagamento == 2:
    print(f'Sua compra será parcelada em 2x de \033[1;32mR${(valor + (valor * 20 / 100)) / 2:.2f}\033[1;32m')
    print(f'Valor final: \033[1;32mR${valor - (valor * 5 / 100):.2f}\033[1;32m')
elif pagamento == 3:
    print(f'Valor final: \033[1;32mR${valor:.2f}\033[1;32m')
elif pagamento == 4:
    parcela = int(input('Informe o número de parcelas: '))
    print(f'Sua compra será parcelada em {parcela}x de \033[1;32mR${(valor + (valor * 20 / 100)) / parcela:.2f}\033[1;32m')
    print(f'Valor final: \033[1;32mR${valor + (valor * 20 / 100):.2f}\033[1;32m')
else:
    print('\033[1;31mOpção Inválida, Tente Novamente\033[1;31m')        