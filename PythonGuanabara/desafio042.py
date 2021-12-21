# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

r1 = float(input('Segmento 1: '))
r2 = float(input('Segmento 2: '))
r3 = float(input('Segmento 3: '))

if r1 < (r2 + r3) and r2 < (r1  + r3) and r3 < (r1 + r2):
    print('Os segmentos podem formar um triângulo')
    
    if r1 == r2 == r3:
        print('É um triângulo \033[1;32mEQUILÁTERO\033[1;32m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um triângulo \033[1;32mISÓSCELES\033[1;32m')  
    else:
        print('É um triângulo \033[1;32mESCALENO\033[1;32m')      
else:
    print('\033[1;31mOs segmentos não podem formar um triângulo\033[1;31m') 