nome = input('Qual é o seu nome?: ').strip().lower()

if nome == 'kayle':
    print('Que nome bonito!')
elif nome == 'maria' or nome == 'pedro' or nome == 'paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'ana cláudia jéssica juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal...')    

print(f'Tenha um bom dia {nome}!')