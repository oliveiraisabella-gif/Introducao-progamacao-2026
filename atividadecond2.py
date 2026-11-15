temperatura = int(input("Me fale uma temperatura: "))
if temperatura < 20:
    print("A temperatura é Fria")
elif temperatura >= 20 and temperatura <= 28:
    print("A temperatura é Normal")
else:
    print("A temperatura é Quente")