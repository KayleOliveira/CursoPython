# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'

cidade = input('Digite o nome da cidade: ').strip()
cidade = cidade.lower()
cidadeS = cidade.split()

if cidadeS[0] == 'santo':
    print('True')
else:
    print('False')

print('santo' == cidadeS[0])
