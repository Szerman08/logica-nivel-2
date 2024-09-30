import tkinter as tk


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


# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")

# Entradas
tk.Label(root, text="Primeiro número:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="Operação (+, -, *, /):").grid(row=1, column=0)
entry_operacao = tk.Entry(root)
entry_operacao.grid(row=1, column=1)

tk.Label(root, text="Segundo número:").grid(row=2, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=2, column=1)

# Botão de calcular
btn_calcular = tk.Button(root, text="Calcular", command=calcular)
btn_calcular.grid(row=3, column=0, columnspan=2)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.grid(row=4, column=0, columnspan=2)

# Iniciar o loop da interface gráfica
root.mainloop()
