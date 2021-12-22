# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Frase: ').strip().upper()
frase = frase.replace(' ', '')

print(f'Frase invertida: {frase[::-1]}')

if frase == frase[::-1]:
    print('É um PALÍNDROMO')
else:
    print('Não é um PALÍNDROMO')    