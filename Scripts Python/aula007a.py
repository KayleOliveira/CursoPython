# nome = input('Qual é o seu nome? ')
# print('Prazer {:=^20}!'.format(nome))

# :20 -> faz o conteúdo ter obrigatoriamente 20 caracteres
# o ^ faz com que o conteúdo fique alinhado ao centro (<, > sao possibilidadesd e alinhamento)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
divi = n1 / n2
diviInt = n1 // n2
poten = n1 ** n2
modulo = n1 % n2

print(f'Soma: {soma}\nSubtração: {sub}\nMultiplicação: {mult}\nDivisão: {divi}\nDivisão Inteira: {diviInt}\nPotência: {poten}\nMódulo: {modulo}')
