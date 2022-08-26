# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []
for i in range(1, 5):
    notas.append(float(input(f"Insira a {i}° nota: ")))

media = sum(notas) / 4
print(f"media:", media)
