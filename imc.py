import tkinter as tk


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


# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de IMC")

# Entradas
tk.Label(root, text="Peso (kg):").grid(row=0, column=0)
entry_peso = tk.Entry(root)
entry_peso.grid(row=0, column=1)

tk.Label(root, text="Altura (m):").grid(row=1, column=0)
entry_altura = tk.Entry(root)
entry_altura.grid(row=1, column=1)

# Botão de calcular
btn_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc)
btn_calcular.grid(row=2, column=0, columnspan=2)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="IMC: ")
label_resultado.grid(row=3, column=0, columnspan=2)

# Iniciar o loop da interface gráfica
root.mainloop()
