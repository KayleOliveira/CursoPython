# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 
        'Ceará FC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print(f'Times: {times}\n')
print(f'Ordem: {sorted(times)}')
print(f'5 primeiros: {times[0:5]}\n')
print(f'4 últimos: {times[-4:]}\n')
chapeco = times.index('Chapecoense')+1
print(f'A chapecoense está na {chapeco}° posição')
