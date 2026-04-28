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


def formatar_real_replace(valor):
    texto = f"R$ {valor:,.2f}"  #padrão EUA: 1,234.56
    texto = texto.replace(",", "X")
    texto = texto.replace(".", ",")
    texto = texto.replace("X", ".")
    return texto

# Uso:
preco = 1234.5
print(formatar_real_replace(preco)) # R$ 1.234,50