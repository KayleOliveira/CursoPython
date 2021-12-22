# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um valor: '))

print('-' * 12)
for i in range(11):
    print(f'{n} * {i:>2} = {n*i}')
print('-' * 12)