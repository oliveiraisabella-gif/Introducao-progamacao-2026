horas = float(input("Digite quantas horas você passa assistindo a telas por dia: "))

if horas < 1:
    print("Espectador Casual")
elif horas >= 1 and horas <= 3:
    print("Maratonista iniciante")
elif horas >= 3 and horas <= 5:
    print("Maratonista Profissional")
else:
    print("Alerta Vermelho!! Desligue a tela e vá ver o sol!")