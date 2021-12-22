# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

m3 = 0
cont = 0

for c in range(0, 501, 3):
    if c % 2 == 1:
        print(c, end=' ')
        cont = cont + 1
        m3 = m3 + c

print(f'\n\nContador: {cont}')
print(f'\nSoma: {m3}')