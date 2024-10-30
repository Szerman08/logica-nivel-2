#16) Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1 = float(input("Digite a 1° nota :"))
nota2 = float(input("Digite a 2° nota :"))

resultado = ((nota1 + nota2) / 2)

print(f" O aluno foi aprovado com a média : {resultado}" )

