num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print('4 not found')
print(num)
print(f'Esta lista tem {len(num)} elementos')


valores = list()

for count in range(0, 5):
    valores.append(int(input('Digite um número: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} está o valor {v}!')