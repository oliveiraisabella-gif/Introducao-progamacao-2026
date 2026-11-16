Moedas = float(input("Quantas Moedas você tem?: "))
Skin = float(input("Qual o valor da skin?: "))

if Moedas > Skin:
    print("Compra realizada! Aproveite sua nova skin")
else:
    print(f"Saldo insuficiente! Faltam {Skin - Moedas:.2f} para você comprar este item")
