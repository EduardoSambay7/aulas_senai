import time
import os
import platform


def shutdown():
    sistema = platform.system().lower()

    try:
        if "windows" in sistema:
            os.system("shutdown /s /t 0")

        elif "linux" in sistema or "darwin" in sistema:
            os.system("shutdown now")

        else:
            print("\nSISTEMA OPERACIONAL NÃO RECONHECIDO")

    except Exception as e:
        print(f"\nErro ao tentar o shutdown: {e}")


def temporizador_com_shutdown():
    try:
        entrada = input("Digite o tempo em segundos para desligar o PC: ")
        segundos = int(entrada)

        while segundos > 0:
            '''Se o usuário digitar 125 segundos, o divmod(125,60) faz o seguinte:
            : divide 125 por 60. 0 60 cabe 2 vezes dentro de 125(esses são os minutos),
            após calcula quanto sobrou da divisão. 125 - 60 (60 x 2 ) = 5 (esses são os segundos)'''
            mins, secs = divmod(segundos, 60)
            timer = f"{mins:02d}:{secs:02d}"

            # Bip nos 10 segundos finais
            #pygame pode tocar um bip em mp3
            bip = "\a" if 0 < segundos <= 10 else ""

            print(f"\rTempo restante: {timer} {bip}", end="", flush=True)

            time.sleep(1)
            segundos -= 1

        print("\n\nIniciando desligamento... Tchau! 🖖")

        shutdown()

    except ValueError:
        print("\nErro: por favor, digite apenas números inteiros.")

    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")


if __name__ == "__main__":
    temporizador_com_shutdown()
