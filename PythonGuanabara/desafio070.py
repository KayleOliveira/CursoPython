# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.

totcompra = mais1000 = valorProdBarato = count = 0
nomeProdBarato = ' '

print('LOJA SUPER BARATÃO')

while True:
    nome = input('Produto: ').strip().capitalize()
    preco = float(input('Preço: R$'))
    totcompra += preco
    if preco > 1000:
        mais1000 += 1
    if count == 0 or preco < valorProdBarato:
        nomeProdBarato = nome
        valorProdBarato = preco
        count += 1 
    choice = ' '
    while choice not in 'SN':
        choice = input('Quer continuar? [S/N]: ').strip().upper()[0]
    
    if choice in 'N':
        break

print(f'O total da compra  foi R${totcompra:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeProdBarato} que custou R${valorProdBarato:.2f}')