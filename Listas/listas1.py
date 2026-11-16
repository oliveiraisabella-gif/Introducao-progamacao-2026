#SE LEMBRE!!!!!! O index começa a contar a aparir do 0, já a contagem normal não

frutas = ["Maçã", "Melancia", "Banana", "Uva","Uva","Uva", "Pera", "Abacaxi"]
print(frutas) #Mostra a lista toda
print(frutas[1]) #Mostra a melancia,pois a contagem começa do 0
print(frutas[:2]) #Mostra até a melancia,pois a contagem a partir desse número especifico começa no 1
print(frutas[2:4]) #o número da esquerda começa do 0,o da direita começa no 1,ou seja,vai mostrar Banana e Uva
print(len(frutas)) #Len mostra a quantidade de itens que determinada lista tem
print(frutas.count("Uva")) #Conta a quantidade de elementos repitidos do negocio que a gnt mencionou (Uva)
print(frutas.index("Abacaxi")) #Conta em que posicao o abacaxi ta (no index)

if "Banana" in frutas:
    print("Banana está em frutas!!") #Se banana estiver em frutas,vai mostrar essa mensagem,use com sabedoria!

fruta_pedido = input("Insira uma fruta: ")
frutas.append(fruta_pedido) #Adiciona um elemento que quem interagiu escreveu
print(frutas) #Vai mostrar a lista com o novo elemento que adicionaram!

fruta_pedido2 = input("Insira uma fruta denovo: ")
frutas.insert(0, fruta_pedido2) #Adiciona do mesmo jeito que o append,MAS você pode escolher a posição que vai ser adicionado
print(frutas)

frutas.remove("Melancia") #Remove o elemento que você escolher
print(frutas)

fruta_removida = frutas.pop(4)
print(f"A fruta {fruta_removida} foi removida da lista")

print(f"Lista atual: {frutas}") #O pop tambem serve para remover,mas alem de voce pode escolher qual posição remover ainda consegue exibir a fruta removida

frutas.clear #Serve para remover os itens da lista