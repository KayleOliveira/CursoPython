# Faça um programa que leia a largura e a altura de uma parede. calcule sua área e a quantidade de tinta nescesária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2

larg = float(input('Digite o valor da largura em metros: '))
alt = float(input('Digite o valor da altura em metros: '))
area = alt * larg

print(f'São nescessárias {area/2:.1f} litros de tinta para pintar uma area de {area:.2}m2')
