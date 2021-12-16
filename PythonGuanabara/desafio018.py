# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

# from math import sqrt

# angulo = float(input('Informe o valor do ângulo: '))
# c_oposto = float(input('Digite o comprimento do cateto oposto: '))
# c_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
# hipotenusa = sqrt(c_oposto**2 + c_adjacente**2)
# print(f'Seno: {c_oposto/hipotenusa:.2f}\nCosseno: {c_adjacente/hipotenusa:.2f}\nTangente: {c_adjacente/c_oposto}')

from math import radians, sin, cos, tan

angulo = float(input('Digite o angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'Seno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}')
