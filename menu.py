import tkinter as tk
from datetime import datetime


def abrir_calculadora():
    calculadora_janela = tk.Toplevel(root)
    calculadora_janela.title("Calculadora")

    def calcular():
        try:
            num1 = float(entry_num1.get())
            operacao = entry_operacao.get()
            num2 = float(entry_num2.get())

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "Erro: Divisão por zero"
            else:
                resultado = "Operação inválida"

            label_resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            label_resultado.config(text="Erro: Entrada inválida")

    tk.Label(calculadora_janela, text="Primeiro número:").grid(row=0, column=0)
    entry_num1 = tk.Entry(calculadora_janela, width=20)
    entry_num1.grid(row=0, column=1)

    tk.Label(calculadora_janela, text="Operação (+, -, *, /):").grid(row=1, column=0)
    entry_operacao = tk.Entry(calculadora_janela, width=20)
    entry_operacao.grid(row=1, column=1)

    tk.Label(calculadora_janela, text="Segundo número:").grid(row=2, column=0)
    entry_num2 = tk.Entry(calculadora_janela, width=20)
    entry_num2.grid(row=2, column=1)

    btn_calcular = tk.Button(calculadora_janela, text="Calcular", command=calcular)
    btn_calcular.grid(row=3, column=0, columnspan=2)

    label_resultado = tk.Label(calculadora_janela, text="Resultado: ")
    label_resultado.grid(row=4, column=0, columnspan=2)

    btn_voltar = tk.Button(calculadora_janela, text="Voltar", command=calculadora_janela.destroy)
    btn_voltar.grid(row=5, column=0, columnspan=2)


def abrir_imc():
    imc_janela = tk.Toplevel(root)
    imc_janela.title("Calculadora de IMC")

    def calcular_imc():
        try:
            peso = float(entry_peso.get())
            altura = float(entry_altura.get())
            imc = peso / (altura ** 2)

            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif 18.5 <= imc < 24.9:
                classificacao = "Peso normal"
            elif 25 <= imc < 29.9:
                classificacao = "Sobrepeso"
            elif 30 <= imc < 34.9:
                classificacao = "Obesidade grau I"
            elif 35 <= imc < 39.9:
                classificacao = "Obesidade grau II"
            else:
                classificacao = "Obesidade grau III"

            label_resultado.config(text=f"IMC: {imc:.2f} - {classificacao}")
        except ValueError:
            label_resultado.config(text="Erro: Entrada inválida")

    tk.Label(imc_janela, text="Peso (kg):").grid(row=0, column=0)
    entry_peso = tk.Entry(imc_janela, width=20)
    entry_peso.grid(row=0, column=1)

    tk.Label(imc_janela, text="Altura (m):").grid(row=1, column=0)
    entry_altura = tk.Entry(imc_janela, width=20)
    entry_altura.grid(row=1, column=1)

    btn_calcular = tk.Button(imc_janela, text="Calcular IMC", command=calcular_imc)
    btn_calcular.grid(row=2, column=0, columnspan=2)

    label_resultado = tk.Label(imc_janela, text="IMC: ")
    label_resultado.grid(row=3, column=0, columnspan=2)

    btn_voltar = tk.Button(imc_janela, text="Voltar", command=imc_janela.destroy)
    btn_voltar.grid(row=4, column=0, columnspan=2)


def abrir_idade():
    idade_janela = tk.Toplevel(root)
    idade_janela.title("Calculadora de Idade")

    def calcular_idade():
        try:
            ano_nascimento = int(entry_ano_nascimento.get())
            nome = entry_nome.get()
            ano_atual = datetime.now().year
            idade = ano_atual - ano_nascimento

            label_resultado.config(text=f"Olá {nome}, sua idade é: {idade}")
        except ValueError:
            label_resultado.config(text="Erro: Entrada inválida")

    tk.Label(idade_janela, text="Ano de Nascimento:").grid(row=0, column=0)
    entry_ano_nascimento = tk.Entry(idade_janela, width=20)
    entry_ano_nascimento.grid(row=0, column=1)

    tk.Label(idade_janela, text="Nome:").grid(row=1, column=0)
    entry_nome = tk.Entry(idade_janela, width=20)
    entry_nome.grid(row=1, column=1)

    btn_calcular = tk.Button(idade_janela, text="Calcular Idade", command=calcular_idade)
    btn_calcular.grid(row=2, column=0, columnspan=2)

    label_resultado = tk.Label(idade_janela, text="Resultado: ")
    label_resultado.grid(row=3, column=0, columnspan=2)

    btn_voltar = tk.Button(idade_janela, text="Voltar", command=idade_janela.destroy)
    btn_voltar.grid(row=4, column=0, columnspan=2)


# Configuração da janela principal
root = tk.Tk()
root.title("Menu Principal")

# Menu de opções
tk.Label(root, text="Escolha uma opção:").grid(row=0, column=0, columnspan=2)

btn_calculadora = tk.Button(root, text="1 - Calculadora", command=abrir_calculadora, width=20)
btn_calculadora.grid(row=1, column=0, columnspan=2)

btn_imc = tk.Button(root, text="2 - IMC", command=abrir_imc, width=20)
btn_imc.grid(row=2, column=0, columnspan=2)

btn_idade = tk.Button(root, text="3 - Idade", command=abrir_idade, width=20)
btn_idade.grid(row=3, column=0, columnspan=2)

# Iniciar o loop da interface gráfica
root.mainloop()
