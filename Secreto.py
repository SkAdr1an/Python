import tkinter as tk
from tkinter import messagebox
import random

# Função para mover o botão "Não" para uma posição aleatória
def move_no_button(event):
    new_x = random.randint(0, root.winfo_width() - no_button.winfo_width())
    new_y = random.randint(0, root.winfo_height() - no_button.winfo_height())
    no_button.place(x=new_x, y=new_y)

# Função para quando o botão "Sim" é clicado
def on_yes_click():
    yes_window = tk.Toplevel(root)
    yes_window.title("Sim!")
    yes_window.geometry("500x300")
    yes_window.configure(bg="lightpink")

    message = tk.Label(yes_window, text="Agora você terá que fazer amor comigo de manhã,\nquando estiver cozinhando o almoço e antes de dormirmos agarradinhos.", font=("Helvetica", 14), bg="lightpink")
    message.pack(pady=20)

    accept_button = tk.Button(yes_window, text="Aceito", font=("Helvetica", 14), command=on_accept_click)
    accept_button.pack(pady=20)

def on_accept_click():
    accept_window = tk.Toplevel(root)
    accept_window.title("Aceito!")
    accept_window.geometry("300x200")
    accept_window.configure(bg="lightblue")

    message = tk.Label(accept_window, text="🌸", font=("Helvetica", 48), bg="lightblue")
    message.pack(pady=20)

# Criação da janela principal
root = tk.Tk()
root.title("Pedido de Namoro")
root.geometry("600x400")
root.configure(bg="white")

# Mensagem inicial
message = tk.Label(root, text="Pi <3 Você quer namorar comigo?", font=("Helvetica", 20), bg="white")
message.pack(pady=50)

# Botão "Sim"
yes_button = tk.Button(root, text="Sim", font=("Helvetica", 14), command=on_yes_click)
yes_button.pack(side=tk.LEFT, padx=50)

# Botão "Não"
no_button = tk.Button(root, text="Não", font=("Helvetica", 14))
no_button.pack(side=tk.RIGHT, padx=50)

# Bind para mover o botão "Não" quando o mouse passar sobre ele
no_button.bind("<Enter>", move_no_button)

root.mainloop()
