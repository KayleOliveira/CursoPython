# Faça um programa que leia uma frase pelo teclado e mostre: 

# + Quantas vezes aparece a letra 'a'
# + Em que posição ela aparece a primeira vez
# + Em que posição ela aparece a última vez

frase = input('Digite uma frase: ').strip().lower()

print(f'Qtd de letras A: {frase.count("a")}')
print(f'Primeira letra A: {frase.find("a") + 1}')
print(f'Última letra A: {frase.rfind("a") + 1}')