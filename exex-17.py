17) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

ano_atual = int(input("Digite o ano atual: "))
nascimento = int(input("Digite o ano de seu nascimento: "))

soma = ano_atual - nascimento
if soma >= 16:
    print("Você pode votar!")
else:
    print("Você não pode votar")
