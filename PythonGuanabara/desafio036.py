# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe seu salário atual: '))
anos = int(input('Informe a quantidade de anos de financiamento: '))* 12
prestacao = casa / anos

if prestacao < salario * (30 / 100):
    print(f'30% do salário: R${salario * (30 / 100):.2f}')
    print(f'Prestação: R${prestacao:.2f}')
    print('\033[1;32mO EMPRESTIMO FOI APROVADO!\033[1;32m')
else:
    print(f'30% do salário: R${salario * (30 / 100):.2f}')
    print(f'Prestação: R${prestacao:.2f}')
    print('\033[1;31mO EMPRESTIMO FOI RECUSADO!\033[1;31m')