# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa

# from math import sqrt
# c_oposto = float(input('Digite o comprimento do cateto oposto: '))
# c_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
# hipotenusa_q = (c_oposto**2 + c_adjacente**2)
# print(f'Comprimento da hipotenusa: {sqrt(hipotenusa_q):.2f}')

import math


c_oposto = float(input('Digite o comprimento do cateto oposto: '))
c_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(c_oposto, c_adjacente)
print(f'Hipotenusa: {hipotenusa}')