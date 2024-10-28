#10. Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa de R$ 700,00 para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.

# Função para calcular o salário final do vendedor
def calcular_salario_final(salario_fixo, comissao_fixa_por_carro, numero_carros_vendidos, valor_total_vendas):
    # Comissão fixa total
    comissao_fixa_total = comissao_fixa_por_carro * numero_carros_vendidos

    # Comissão percentual (5% do valor total das vendas)
    comissao_percentual = valor_total_vendas * 0.05

    # Salário final
    salario_final = salario_fixo + comissao_fixa_total + comissao_percentual

    return salario_final


# Leitura dos dados
numero_carros_vendidos = int(input("Digite o número de carros vendidos: "))
valor_total_vendas = float(input("Digite o valor total das vendas: R$ "))
salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
comissao_fixa_por_carro = 700.00  # Comissão fixa por carro vendido

# Cálculo do salário final
salario_final = calcular_salario_final(salario_fixo, comissao_fixa_por_carro, numero_carros_vendidos,
                                       valor_total_vendas)

# Exibindo o salário final
print(f"O salário final do vendedor é: R$ {salario_final:.2f}")
