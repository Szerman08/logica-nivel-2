#15) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.


while True:
    # Solicita ao usuário o número de maçãs compradas
    quantidade = int(input("Digite o número de maçãs compradas (ou 0 para sair): "))

    # Verifica se o usuário deseja sair
    if quantidade == 0:
        print("Programa encerrado.")
        break

    # Define o preço por maçã com base na quantidade comprada
    if quantidade < 12:
        preco_por_maca = 1.30
    else:
        preco_por_maca = 1.00

    # Calcula o custo total
    custo_total = quantidade * preco_por_maca

    # Exibe o custo total da compra
    print(f"O custo total da compra é: R$ {custo_total:.2f}\n")
