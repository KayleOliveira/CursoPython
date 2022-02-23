count = 1

while True:
    if count <= 10:
        print(f'{count}', end=' ')
        count += 1
    else:
        break
print('Laço acabou!', end=' ')    

n = soma = count = 0
while n != 999:
    n = int(input('Informe um número: '))
    if n == 999:
        break
    count += 1
    soma += n
print(f'Contador: {count}')
print(f'Soma: {soma}')