import time
import sys

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

# Texto divertido
texto_divertido = "Deveras importante meu amigo, tenha paciência e calma. Saiba que você é amado por Deus"

animate_text(texto_divertido)
