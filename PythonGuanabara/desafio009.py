# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada

n = int(input('Digite um valor: '))

# o range aquie deve ser 11 e nao dez pois, além das 10 mult ainda tem a mult por zero
print('-' * 12)
for i in range(11):
    print(f'{n} * {i:>2} = {n*i}')
print('-' * 12)