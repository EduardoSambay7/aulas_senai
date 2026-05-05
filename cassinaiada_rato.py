import tkinter as tk
from tkinter import ttk
import random
import pygame

# Inicializa som
pygame.mixer.init()

# Configurações
simbolos = ["🐭", "🧀", "🍓", "💫", "🍊"]
saldo = 50.0

# Função som
def tocar_som():
    try:
        pygame.mixer.music.load("")
        pygame.mixer.music.play()
    except:
        print("Erro ao tocar som")

# Função girar
def girar():
    global saldo

    aposta = aposta_var.get()

    if aposta > saldo:
        resultado_label.config(text="Saldo insuficiente!", fg="red")
        return

    saldo -= aposta

    resultado = [random.choice(simbolos) for _ in range(3)]

    # Atualiza slots
    for i, slot in enumerate(slots):
        slot.config(text=resultado[i])

    # Vitória
    if resultado[0] == resultado[1] == resultado[2]:
        premio = aposta * 5
        saldo += premio
        resultado_label.config(text=f"🐭 JACKPOT! +R${premio}", fg="#00ff88")
        tocar_som()
    else:
        resultado_label.config(text="😓 Nada dessa vez...", fg="white")

    saldo_label.config(text=f"Saldo: R${saldo:.2f}")

# Janela
janela = tk.Tk()
janela.title("🎰 Cassino do Rato")
janela.geometry("420x320")
janela.configure(bg="#1a1a1a")
janela.resizable(False, False)

# Estilo
style = ttk.Style()
style.theme_use("default")

# Título
titulo = tk.Label(
    janela,
    text="🎰 CASSINO DO RATO 🐭",
    font=("Arial", 18, "bold"),
    fg="#ffd700",
    bg="#1a1a1a"
)
titulo.pack(pady=10)

# Frame slots
frame_slots = tk.Frame(janela, bg="#1a1a1a")
frame_slots.pack(pady=10)

slots = []
for _ in range(3):
    lbl = tk.Label(
        frame_slots,
        text="❓",
        font=("Arial", 32),
        width=2,
        bg="#000000",
        fg="#00ffcc",
        relief="ridge",
        bd=4
    )
    lbl.pack(side="left", padx=8)
    slots.append(lbl)

# Resultado
resultado_label = tk.Label(
    janela,
    text="Faça sua aposta e gire!",
    font=("Arial", 12),
    fg="white",
    bg="#1a1a1a"
)
resultado_label.pack(pady=5)

# Frame aposta
frame_aposta = tk.Frame(janela, bg="#1a1a1a")
frame_aposta.pack(pady=5)

tk.Label(
    frame_aposta,
    text="Aposta:",
    font=("Arial", 12),
    fg="white",
    bg="#1a1a1a"
).pack(side="left", padx=5)

aposta_var = tk.IntVar(value=5)

spin_aposta = tk.Spinbox(
    frame_aposta,
    from_=1,
    to=100,
    textvariable=aposta_var,
    width=5,
    font=("Arial", 12),
    justify="center"
)
spin_aposta.pack(side="left")

# Saldo
saldo_label = tk.Label(
    janela,
    text=f"Saldo: R${saldo:.2f}",
    font=("Arial", 12, "bold"),
    fg="#00ff88",
    bg="#1a1a1a"
)
saldo_label.pack(pady=5)

# Botão girar
botao = tk.Button(
    janela,
    text="🎲 GIRAR",
    font=("Arial", 14, "bold"),
    bg="#ffd700",
    fg="black",
    activebackground="#ffcc00",
    command=girar
)
botao.pack(pady=15, ipadx=10, ipady=5)

# Loop
janela.mainloop()
