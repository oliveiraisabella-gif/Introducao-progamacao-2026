preco = float(input("Me fale o preço da mercadoria: "))
desconto = float(input("Me fale o percentual de desconto: "))

valor_desconto = preco * (desconto / 100)
preco_pagar =  preco - valor_desconto

print(f"Valor do Desconto: {valor_desconto:.2f}")
print(f"Preço a pagar: {preco_pagar:.2f}")