17) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).


nome = str(input("Digite seu nome: "))
data = int(input("Digite o ano atual: "))
nascimento = int(input("Digite o ano do seu nascimento: "))

soma = data-nascimento
print("Olá", nome, "a sua idade é:",soma)
