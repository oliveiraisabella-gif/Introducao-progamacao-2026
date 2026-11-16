notas = []

for _ in range(5):
    nota = float(input("Nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"Menor: {min(notas):.1f}")
print(f"Maior: {max(notas):.1f}")
print(f"Media: {media:.1f}")