import random
#10. JOGO DE ADVINHAÇÃO
print("===Advinhe o Número ===\n")
secreto = random.randint(1, 100)
tentativas = 0
palpite = 0
while palpite != secreto:
    palpite = int(input("Seu palpite (1-100): "))
    tentativas += 1

    if palpite < secreto:
        print("Muito Baixo!")
    elif palpite > secreto:
        print("Muito Alto!")
    else:
        print(f"Parabéns! Acertou em {tentativas} tentativas!")
                


