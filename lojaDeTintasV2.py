"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    · comprar apenas latas de 18 litros;
    · comprar apenas galões de 3,6 litros;
    · misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
from math import ceil, floor

tamanhoArea = float(input("Insira a área em metros quadrados: "))
litros = tamanhoArea / 6
litroFolga = litros * 1.1
galoes = ceil(litros / 3.6)
latas = ceil(litros / 18)
custoLatas = latas * 80
custoGalao = galoes * 25
print("litros:", litros)
print("Quantidades de latas:", int(latas))
print("custo(apenas latas):", custoLatas)
print("\nQuantidades de galões:", int(galoes))
print("custo(apenas galoes):", custoGalao)

latasFolga = litroFolga / 18
resto = latasFolga - floor(latasFolga)

if resto >= 0.8 or resto == 0:
    latasFolga = ceil(latasFolga)
    galoesFolga = 0
else:
    latasFolga = floor(latasFolga)
    galoesFolga = ceil((litroFolga - latasFolga * 18) / 3.6)

custoFolga = latasFolga * 80 + galoesFolga * 25

print("\nlitros com folga:", litroFolga)
print("Quantidades de latas:", latasFolga)
print("Quantidades de galões:", galoesFolga)
print("custo:", custoFolga)
