# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = input('Digite a expressão: ')
abre = fecha = 0
for pos, index in enumerate(expressao):
    if '(' in expressao[pos]:
        abre += 1
    if ')' in expressao[pos]:
        fecha += 1
if abre == fecha:
    print('Expressao Válida')
else:
    print('Expressao Inválida')


# Fiz abaixo a versão do Guanabara pois a lógica foi melhor
expr = input('Digite uma expressão: ')
pilha = []
for simb in expr:
    # se houver um '(' então adicione-o à pilha
    if simb == '(':
        pilha.append('(')  
    elif simb == ')':
        # caso encontre um ')' e a pilha não esteja vazia, elimine o único item que está na pilha [já que é o '(' ]
        if len(pilha) > 0:
            pilha.pop()
        # caso não, adicione o ')' ao conjunto de pilha
        else:
            pilha.append(')')
            break

# caso o len de pilha seja != 0 significa diretamente que a qtd de '(' e ')' não são equivalentes
if len(pilha) == 0:
    print('Expressão Válida')
else:
    print('Expressão Inválida')    

