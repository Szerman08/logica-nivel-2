#9) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.


# Função para calcular o custo final ao consumidor
def calcular_custo_final(custo_fabrica):
    percentual_distribuidor = 0.28  # 28%
    percentual_impostos = 0.45       # 45%

    # Calculando as comissões e impostos
    comissao_distribuidor = custo_fabrica * percentual_distribuidor
    impostos = custo_fabrica * percentual_impostos

    # Calculando o custo final ao consumidor
    custo_final = custo_fabrica + comissao_distribuidor + impostos

    return custo_final

# Leitura do custo de fábrica
custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))

# Cálculo do custo final
custo_final = calcular_custo_final(custo_fabrica)

# Exibindo o custo final ao consumidor
print(f"O custo final ao consumidor é: R$ {custo_final:.2f}")
