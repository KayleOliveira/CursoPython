# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da
# passagem, cobrando R$0.50/km para viagens de até 200km e R$0.45 para viagens mais longas

distancia = float(input('Informe a distância (km): '))

if distancia > 200:
    print(f'Valor da passagem: R${distancia * 0.45:.2f}')
else:
    print(f'Valor da passagem: R${distancia * 0.5:.2f}')