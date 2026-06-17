resposta = input("O que você aprendeu hoje? ")

with open("bordo.txt", "a") as caderno:
    caderno.write(f"{resposta}\n")

print("\nAnotacao salva com sucesso!\n")

print("--- Historico de Aprendizado ---")

try:
    with open("bordo.txt", "r") as caderno:
        for numero, linha in enumerate(caderno, start=1):
            print(f"{numero}: {linha.strip()}")
except FileNotFoundError:
    print("Caderno ainda vazio, escreva a primeira anotacao acima!")
    