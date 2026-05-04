import tkinter as tk
import random

# Configurações
simbolos = ["🍵","🧁", "🍓", "💫", "🍊"]
saldo = 20.0
custo_giro = 2

#Função de girar
def girar():
    global saldo

    if saldo < custo_giro:
        resultado_label.config(text="Saldo insuficiente!", fg="red")
        return

  saldo -= custo_giro

resultado = [random.choice(simbolos) for _ in range(3)]

#Atualiza os slots
slot1.config(text=resultado[0])
slot2.config(text=resultado[1])
slot3.config(text=resultado[2])

# Verifica vitória 
if resultado[0] == resultado[1] == resultado[2]:
    premio = 20
    saldo += premio
    resultado_label.config(text=f"🎆 JACKPOT! +R$ {premio}", fg="green")
else:
    resultado_label.config(text="😓 Tente novamente...", fg="black")

saldo_label.config(text=f"Saldo: R${saldo:.2f}")

#janela principal

janela = tk.Tk()
janela.title("🎰 Máquina de Slots - Duzera")
janela.geometry("350x250")
janela.resizable(False, False)

#título 
titulo = tk.Label(janela, text="🎰 Slots Duzera", font("Arial", 16, "bold"))
