""" 
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    · o produto do dobro do primeiro com metade do segundo.
    · a soma do triplo do primeiro com o terceiro.
    · o terceiro elevado ao cubo. 
"""

num1 = int(input("Insira um valor inteiro: "))
num2 = int(input("Insira outro valor inteiro: "))
num3 = float(input("Insira um valor real: "))

print("o produto do dobro do primeiro com metade do segundo:", num1 * num2)
print("a soma do triplo do primeiro com o terceiro:", 3 * num1 + num3 / 2)
print("o terceiro elevado ao cubo:", num3 ** 3)
