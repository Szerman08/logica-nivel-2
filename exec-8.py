#Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

# Função para calcular o novo salário
def calcular_novo_salario(salario_atual, percentual_reajuste):
    # Calculando o aumento
    aumento = salario_atual * (percentual_reajuste / 100)

    # Calculando o novo salário
    novo_salario = salario_atual + aumento

    return novo_salario


# Leitura do salário atual
salario_atual = float(input("Digite o salário mensal atual do funcionário: R$ "))

# Leitura do percentual de reajuste
percentual_reajuste = float(input("Digite o percentual de reajuste: "))

# Cálculo do novo salário
novo_salario = calcular_novo_salario(salario_atual, percentual_reajuste)

# Exibindo o novo salário
print(f"O novo salário do funcionário é: R$ {
