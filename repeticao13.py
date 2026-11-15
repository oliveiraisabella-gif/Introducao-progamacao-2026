soma = 0

while True:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    soma = soma + num

print(f"Soma total: {soma}")