# Lê a temperatura em graus Fahrenheit
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Calcula a temperatura em graus Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Imprime a temperatura em graus Celsius com duas casas decimais
print(f"A temperatura em graus Celsius é: {celsius:.2f}")
