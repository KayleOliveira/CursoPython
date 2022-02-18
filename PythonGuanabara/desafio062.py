# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Primeiro termo: '))
termo = primeiro
total = 0
razao = int(input('Razão: '))
count = 1
mais = 10

while mais != 0:
    total += mais
    while count <= total:
        print(f'{termo} -> ', end=' ')
        termo += razao
        count += 1

    print('PAUSE')

    mais = int(input('Quantos termos queres mostrar a mais? '))
print(f'Total de termos: {total}')
print('FINISH')