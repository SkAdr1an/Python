Calculadora com interface.py 

import tkinter as tk 
def calcular():
    try:
        resultado = eval(entry.get())
        label_resultado.config(text=f"Resultado: {resultado}")
    except Exception as e:
        label_resultado.config(text=f"Erro: {e}")

root = tk.Tk()
root.title("Albert Adrian")

entry = tk.Entry(root, width=25, borderwidth=2)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, command=calcular)
    else:
        button = tk.Button(root, text=text, command=lambda t=text: entry.insert(tk.END, t))
    button.grid(row=row, column=col, padx=4, pady=5)

label_resultado = tk.Label(root, text="Soma:")
label_resultado.grid(row=5, column=0, columnspan=4, padx=10, pady=10) 

root.mainloop()
