# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso

# – Entre 18,5 e 25: Peso Ideal

# – 25 até 30: Sobrepeso

# – 30 até 40: Obesidade

# – Acima de 40: Obesidade Mórbida

peso = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura (m): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'IMC: {imc:.1f}\n\033[1;31mABAIXO DO PESO\033[1;31m')
elif imc < 25:
    print(f'IMC: {imc:.1f}\n\033[1;32mPESO IDEAL\033[1;32m')
elif imc < 30:
    print(f'IMC: {imc:.1f}\n\033[1;33mACIMA DO PESO\033[1;33m') 
elif imc < 40:
    print(f'IMC: {imc:.1f}\n\033[1;31mOBESIDADE\033[1;31m')
else:
    print(f'IMC: {imc:.1f}\n\033[1;31mOBESIDADE MÓRBIDA\033[1;31m')           