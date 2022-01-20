import random

def escolher_ganhador(*participantes):
    return random.choice(participantes)

if __name__ == "__main__":
    # Exemplo de uso
    ganhador = escolher_ganhador("débora", "thiago","davi","gabriela")
    print(ganhador)