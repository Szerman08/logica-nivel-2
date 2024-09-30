import tkinter as tk
from datetime import datetime


def calcular_idade():
    try:
        ano_nascimento = int(entry_ano_nascimento.get())
        nome = entry_nome.get()
        ano_atual = datetime.now().year
        idade = ano_atual - ano_nascimento

        label_resultado.config(text=f"Olá {nome}, sua idade é: {idade}")
    except ValueError:
        label_resultado.config(text="Erro: Entrada inválida")


# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Idade")

# Entradas
tk.Label(root, text="Ano de Nascimento:").grid(row=0, column=0)
entry_ano_nascimento = tk.Entry(root)
entry_ano_nascimento.grid(row=0, column=1)

tk.Label(root, text="Nome:").grid(row=1, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=1, column=1)

# Botão de calcular
btn_calcular = tk.Button(root, text="Calcular Idade", command=calcular_idade)
btn_calcular.grid(row=2, column=0, columnspan=2)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.grid(row=3, column=0, columnspan=2)

# Iniciar o loop da interface gráfica
root.mainloop()
