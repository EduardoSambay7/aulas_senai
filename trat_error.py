while True:
    try:
        numero = int(input("Insira um número inteiro: "))
        resultado = numero * 2
        break

    except ValueError:
        print("Calma,Digite apenas números inteiros!")

print(f"Resultado: {resultado}")