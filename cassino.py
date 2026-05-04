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
slot1.config(text.
