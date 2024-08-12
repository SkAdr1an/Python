import time
from datetime import datetime, timedelta
import tkinter as tk

# Solicita ao usuário que digite seu nome e data de nascimento completa
nome = input("Digite seu nome: ")
ano = int(input("Digite o ano de nascimento (YYYY): "))
mes = int(input("Digite o mês de nascimento (MM): "))
dia = int(input("Digite o dia de nascimento (DD): "))

# Solicita a hora e minuto de nascimento, se o usuário souber
hora = input("Digite a hora de nascimento (HH) ou pressione Enter se não souber: ")
minuto = input("Digite o minuto de nascimento (MM) ou pressione Enter se não souber: ")

# Define valores padrão para hora e minuto se não forem fornecidos
hora = int(hora) if hora else 0
minuto = int(minuto) if minuto else 0

# Expectativa de vida média no Brasil em anos
expectativa_vida = 75

# Data e hora de nascimento do usuário
nascimento = datetime(ano, mes, dia, hora, minuto)

# Data e hora esperada de morte
morte_esperada = nascimento + timedelta(days=expectativa_vida * 365.25)

# Calcula o tempo restante em segundos a partir da data e hora atual
agora = datetime.now()
tempo_restante = morte_esperada - agora
segundos_restantes = int(tempo_restante.total_seconds())

print(f"{nome}, você tem aproximadamente {int(tempo_restante.days / 365.25)} anos restantes de vida.")

# Função para formatar o tempo restante
def format_time(seconds):
    days = int(seconds // (24 * 3600))
    seconds = seconds % (24 * 3600)
    hours = int(seconds // 3600)
    seconds %= 3600
    minutes = int(seconds // 60)
    seconds %= 60
    return days, hours, minutes, seconds

# Função para atualizar o cronômetro da vida contínuo
def update_cronometro():
    global segundos_restantes
    if segundos_restantes > 0:
        dias, horas, minutos, segundos = format_time(segundos_restantes)
        dias_str = f"{dias}d"
        horas_str = f"{horas:02d}"
        minutos_str = f"{minutos:02d}"
        segundos_str = f"{segundos:02d}"
        label_dias.config(text=dias_str)
        label_horas.config(text=horas_str)
        label_minutos.config(text=minutos_str)
        label_segundos.config(text=segundos_str)
        segundos_restantes -= 1
        root.after(1000, update_cronometro)
    else:
        label_dias.config(text="0d")
        label_horas.config(text="00")
        label_minutos.config(text="00")
        label_segundos.config(text="00")
        print("Tempo de vida estimado acabou.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Cronômetro da Vida")
root.geometry("600x300")
root.configure(bg='black')

label_dias = tk.Label(root, text="", font=("Helvetica", 48), fg="white", bg="black")
label_dias.pack(side=tk.LEFT, padx=10)

label_horas = tk.Label(root, text="", font=("Helvetica", 48), fg="white", bg="black")
label_horas.pack(side=tk.LEFT, padx=10)

label_colon1 = tk.Label(root, text=":", font=("Helvetica", 48), fg="white", bg="black")
label_colon1.pack(side=tk.LEFT)

label_minutos = tk.Label(root, text="", font=("Helvetica", 48), fg="white", bg="black")
label_minutos.pack(side=tk.LEFT, padx=10)

label_colon2 = tk.Label(root, text=":", font=("Helvetica", 48), fg="white", bg="black")
label_colon2.pack(side=tk.LEFT)

label_segundos = tk.Label(root, text="", font=("Helvetica", 48), fg="white", bg="black")
label_segundos.pack(side=tk.LEFT, padx=10)

# Inicia o cronômetro da vida contínuo
update_cronometro()
root.mainloop()
