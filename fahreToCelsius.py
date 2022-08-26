# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

tempFahre = float(input("Insira a temperatura em °F: "))
tempCelsi = 5 / 9 * (tempFahre - 32)

print("temperatura em °C:", tempCelsi)