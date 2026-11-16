#Isso é para números ímpares

fim = int(input("Digite o último número da sequência: "))
num = 1
while num <= fim:
    if num % 2 == 0:
        print(num)
    num = num + 1