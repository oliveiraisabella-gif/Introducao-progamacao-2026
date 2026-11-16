import random

participantes = []

while True:
    nome = input("Nome (ENTER encerra): ")
    if nome == "":
        break
    participantes.append(nome)

if participantes:
    ganhador = random.choice(participantes)
    print(f"Ganhador: {ganhador}")

    #Sorteio de rifa