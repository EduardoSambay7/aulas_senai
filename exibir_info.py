def exibir_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

#Criamos um dicinário vazio para armazenar as entradas

info_usuario = {}

print("digite as informações (ou 'sair' na chave para encerrar)")

while True:
    chave = input("Nome do campo (ex: Profissão): ")
    if chave.lower() == "sair":
        break
    valor = input(f"Valor para {chave}: ")
    info_usuario[chave] = valor

# Usamos ** para desempacotar o dicionário como argumentos


exibir_info(**info_usuario)

