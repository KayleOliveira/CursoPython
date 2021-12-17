# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo

r1 = float(input('Segmento 1: '))
r2 = float(input('Segmento 2: '))
r3 = float(input('Segmento 3: '))

menor = r1
maior1 = r1
maior2 = r1
maiores = maior1 + maior2

if r1 < (r2 + r3) and r2 < (r1  + r3) and r3 < (r1 + r2):
    print('Os segmentos podem formar um triângulo')
else:
    print('Os segmentos não podem formar um triângulo')    













# if s2<s1 and s2<s3:
#     menor = s2
#     maior1 = s1
#     maior2 = s3
# if s3<s1 and s3<s2:
#     menor = s3
#     maior1 = s1
#     maior2 = s2

# if menor > maiores:
#     print('Os segmentos podem formar um triângulo!')
# else:
#     print('Os segmentos não podem formar um triângulo!')