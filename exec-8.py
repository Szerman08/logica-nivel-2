# Leitura dos dados
total_eleitores = int(input('Digite o número total de eleitores: \n'))
votos_brancos = int(input('Digite o número de votos brancos: \n'))
votos_nulos = int(input('Digite o número de votos nulos: \n'))
votos_validos = int(input('Digite o número de votos válidos: \n'))

# Cálculo dos percentuais
brancos = (votos_brancos / total_eleitores) * 100
nulos = (votos_nulos / total_eleitores) * 100
validos = (votos_validos / total_eleitores) * 100

# Exibição dos resultados
print(f'\n\nPercentual de votos brancos: {brancos:}%\n')
print(f'Percentual de votos nulos: {nulos:}%\n')
print(f'Percentual de votos válidos: {validos:}%\n')
