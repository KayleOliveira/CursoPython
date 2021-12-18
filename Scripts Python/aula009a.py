frase = 'Curso em Video Python'
#print a letra na posição 3
print(frase[3])
#print da posição 3 à 13
print(frase[3:13])
#print da posição 0 à 13
print(frase[:13])
#print da posição 13 à última
print(frase[13:])
#print da posição 1 à 15
print(frase[1:15])
#print da posição 1 à 15, pulando de 2 em 2
print(frase[1:15:2])
#print da posição 1 até o final, pulando de 2 em 2
print(frase[1::2])
#print da posição 0 até o final, pulando de 2 em 2
print(frase[::2])
#.count conta quantos caracteres estao presentes da variável
print(frase.count('o'))
#.upper leva todos os caracteres para maiúsculo
print(frase.upper())
#.lower leva todos os caracteres para minúsculo
print(frase.lower())
#.capitalize transforma o primeiro caractere em maiúsculo
print(frase.capitalize())
#.title transforma os primeiros caracteres de cada palavra em maiúsculo
print(frase.title())
#len() retorna o tamanho da variável
print(len(frase))
#.strip elimina todos os espaços colocados no começo e no final da variável (pode variar entre .rstrip ou lstrip)
print(frase.strip())
#.replace substitui o 'a' por 'b'
print(frase.replace('Python', 'JavaScript'))
# 'a' in frase verifica se frase contém 'a', retorna um bool
print('Curso' in frase)
#.find retorna a posição de 'a' caso exista em frase, caso não, retorna -1
print(frase.find('Curso'))
#.split separa em outros arrays onde tiver 'espaço vazio' (default)
print(frase.split())
#'a'.join(frase) faz com que frase se junte novamente substituindo ' ' por '-'
print('-'.join(frase)) 