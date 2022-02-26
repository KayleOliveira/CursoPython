#Criando uma tupla

lanche = 'Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'

for comida in lanche:
    print(comida)

for count in range(0, len(lanche)):
    print(lanche[count])

#Para mostrar de forma organizada (alfabética)
print(sorted(lanche))

#Deletar tupla
del(lanche)