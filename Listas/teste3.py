import random

nomes = ["Ana", "Bia", "Caio", "Davi"]
random.shuffle(nomes)
ganhador = random.choice(nomes)
print(ganhador) #Sorteio