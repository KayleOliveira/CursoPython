# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = float(input('Digite o preço atual do produto: '))
por = float(input('Digite o valor da porcentagem: '))

print(f'O preço final do produto com 5 porcento de desconto é: R${n-(n*por/100)}')

