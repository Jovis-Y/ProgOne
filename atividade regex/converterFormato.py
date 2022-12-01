"""
2) Faça uma função que recebe um string e retorna o string com os números de telefones transformados para um único formato:
(91) 91234 5678
"""
import re

def transform(text):
  patterns = [r"\(0\d{2}\)\d{5} \d{4}", r"\(\d{2}\) \d{5}-\d{4}", r"\d{2} \d{5} \d{4}", r"\d{2}-\d{5}-\d{4}"]
  
  if re.fullmatch(patterns[0], text):
    newtxt = f"({text[2:4]}) {text[5:10]} {text[11:]}"
  elif re.fullmatch(patterns[1], text) or re.fullmatch(patterns[2], text):
    newtxt = f"({text[0:2]}) {text[3:8]} {text[9:]}"
  elif re.fullmatch(patterns[3], text):
    newtxt = f"({text[1:3]}) {text[5:10]} {text[11:]}"
  return string.replace(text, newtxt)

regex = r"\(0\d{2}\)\d{5} \d{4}|" + r"\(\d{2}\) \d{5}-\d{4}|" + r"\d{2} \d{5} \d{4}|" + r"\d{2}-\d{5}-\d{4}"

string = input("Digite um texto com números: ")
lista = re.findall(regex, string)

for texto in lista:
  string = transform(texto)

print(string)
