# # geral = "Essa variável posso chamar onde quiser"
# # def  minha_funcao():
# #     print("Essa é minha função")
# #     local = "Essa váriavel só pode ser usada localmente, na função"
# #     true 

# # # chamando a minha função
# # minha_funcao()
# # print(local)
# # # print(local)
# # print(geral)

# nome = "Alan"  #Global

# def saudacao():
#     sobrenome = "Code" # Local
#     print(f"Olá, {nome} {sobrenome}")

# saudacao()

# def somar(n1, n2): #n1 e n2 são parâmetros
#     print(f"A soma é {n1 + n2}")

# somar(6, 40) #6 e 40 são argumentos


def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Uso:
preco_hospedagem = 49.9
print(formatar_real(preco_hospedagem)) # R$ 49,90