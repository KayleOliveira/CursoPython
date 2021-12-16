# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere: US$1,00 == R$3,27

n = float(input('Digite quanto de dinheiro tens na carteira: R$'))

print(f'Com {n} reais, poderais comprar: US${n/5.61:.2f}')
print(f'Com {n} reais, poderais comprar: EU${n/6.35:.2f}')
print(f'Com {n} reais, poderais comprar: Y${n/0.049:.2f}')
print(f'Com {n} reais, poderais comprar: CAD${n/4.41:.2f}')
