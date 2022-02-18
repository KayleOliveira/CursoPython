# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

total = 0

count = 0

while count != 999:
    count = int(input('Digite [999] para parar: '))
    total += count

    if count == 999 :
        total = total - 999

print(f'Total: {total}')

# ESTA SOLUÇÃO PODE NÃO SER A MELHOR, NA AULA 15 A MELHOR SOLUÇÃO SERÁ APRESENTADA...