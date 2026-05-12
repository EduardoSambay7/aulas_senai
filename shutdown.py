import time
import sys
import os
import plataform

def shutdown():
    sistema = platfomr.system().lower()
    try:
        if "windows" in sistema:
            os.system("shutdown /s /t 0")
        elif "linux" in sistema or "darwin" in sistema:
            os.system("shutdown now")

        else:
            print("\nSISTEMA OPERACIONAL NÃO RECONHECIDO")
    except Exception as e:
        print(f"\n Erro ao tentar o Shutdown")
