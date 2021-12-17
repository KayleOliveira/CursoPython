# Escreva um programa que leia a velocidade de um carro em km

# + Se ele ultrapassar 80km/h, mostre uma mensagem na tela dizendo que ele foi multado
# + A multa vai custar R$7.00/km acima do limite

velocidade = float(input('Digite a velocidade (km): '))

if velocidade > 80:
    print(f'Voçê foi multado em R${7 * (velocidade - 80):.2f}')
else:
    print(f'Dirija com segurança')