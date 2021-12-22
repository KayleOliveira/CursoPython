

for c in range(6, 0, -1):
    print(c)

#de 0 á 6, pulando de 2 em 2
for c in range(0, 7, 2):
    print(c)

inicio = int(input('Digite um número: '))
fim = int(input('Digite um número: '))
passo = int(input('Digite um número: '))

for c in range(inicio, fim+1, passo):
    print(c)