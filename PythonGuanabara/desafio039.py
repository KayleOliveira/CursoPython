# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

ano = int(input('Informe seu ano de nascimento: '))
sexo = input('Informe seu sexo: ').strip().lower()
idade = datetime.date.today().year - ano

if sexo == 'masculino' or sexo == 'm' or sexo == 'male':
    if idade < 18:
        print(f'Ainda faltam {18 - idade} ano(s) para seu alistamento militar')
        print(f'Seu alistamento será em {ano + 18}')
    elif idade == 18:
        print(f'Este ano voçê deverá se alistar')
    else:
        print(f'Seu alistamento está atrasado {idade - 18} ano(s). Aliste-se urgentemente!')
        print(f'Seu alismento foi em {ano + 18}')
else:
    print('\033[1;31mPor não ser homem seu alistamento não é obrigatório!\033[1;31m')