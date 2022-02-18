# for c in range(1, 10):
#     print(c)

c = 1
while c < 10:
    print(c)
    c += 1

print('FIM')

n = 1

while n != 0:
    n = int(input('Digite um valor: '))

num = 1
pares = 0
impares = 0
while num != 0:
    num = int(input('Digite um número: '))
    if num != 0:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1    

print(f'Qtd pares: {pares}')
print(f'Qtd impares: {impares}')