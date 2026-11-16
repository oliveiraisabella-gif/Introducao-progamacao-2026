#Faz uma soma com números que não temos informação ainda,os numeros são variaveis

n = 1
soma = 0
while n <= 10:
    num = int(input(F"Digite o {n}º número: "))
    soma= soma + num
    n = n + 1
print(f"Soma = {soma}")