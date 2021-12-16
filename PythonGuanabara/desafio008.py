# Escreva um programa que leia um valor em metros e exiba-o em centímetros e milímetros

n = float(input('Digite o valor em metros: '))

print(f'Kilometro: {n/100}km\nHectometro: {n/100}hm\nDecâmetro: {n/10}dam\nMetros: {n}m\nDecímetro: {n*10}dm\nCentímetros: {n*100}cm\nMilímetros: {n*1000}mm')
