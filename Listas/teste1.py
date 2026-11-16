linguagens = ["Python", "C", "Java"]
procurar = "C"

if procurar in linguagens:
    i = linguagens.index(procurar)
    print(f"Encontrado no índice {i}")
else:
    print("Não Encontrado")