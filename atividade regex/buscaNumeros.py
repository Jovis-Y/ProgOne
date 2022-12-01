"""
1) Escreva uma RE para encontrar números de telefone do tipo:
    (091)91234 5678
    91 91234 5678
    91-91234-5678
    (91) 91234-5678
"""
import re

regex = r"\(0\d{2}\)\d{5} \d{4}|" + r"\(\d{2}\) \d{5}-\d{4}|" + r"\d{2} \d{5} \d{4}|" + r"\d{2}-\d{5}-\d{4}"
numero = input("Digite o número de telefone: ")

lista = re.findall(regex, numero)

for n in lista:
    print(n)
