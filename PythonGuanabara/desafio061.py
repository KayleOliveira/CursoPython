# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Primeiro termo: '))
termo = primeiro
razao = int(input('Razão: '))
count = 1
decimo = termo + (10 - 1) * razao

for c in range(termo, decimo + razao, razao):
    print(c, end=' -> ')
 
while count <= 10:
    print(f'{termo} -> ', end=' ')
    termo += razao
    count += 1

print('FINISH')