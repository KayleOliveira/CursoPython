# Digite um código que leia uma informação e apresente todas os .is

index = input('Digite algo: ')
print(type(index))

print(f'é alfabetico? {index.isalpha()}\n')

print(f'é numérico? {index.isnumeric()}\n')

print(f'é printável? {index.isprintable()}\n')

print(f'é alfa-numérico? {index.isalnum()}\n')

print(f'é ascii? {index.isascii()}\n')

print(f'é decimal? {index.isdecimal()}\n')

print(f'é digito? {index.isdigit()}\n')

print(f'é tudo maiúsculo? {index.isupper()}\n')

print(f'é tudo minúsculo? {index.islower()}\n')

print(f'é um espaço? {index.isspace()}\n')

print(f'é capitalizada? {index.istitle()}\n')

print(f'é um identificador? {index.isidentifier()}\n')
