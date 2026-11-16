salario = float(input("Me fale seu Salário: "))
porcentagem = float(input("Me fale a porcentgem do aumento: "))

aumento = salario * (porcentagem / 100)
salario_aumentado = salario + aumento

print(f"O valor do salario agora é {salario_aumentado:.2f}, e o valor do aumento é {aumento:.2f}!!")