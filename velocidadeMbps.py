"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de 
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link 
(em minutos). 
"""

tamanhoArquivo = float(input("Insira o tamanho do arquivo em MB: ")) * 8
velocidade = float(input("Insira a velocidade em Mbps: "))
tempo = tamanhoArquivo / velocidade / 60

print("tempo em minutos para o download completo:", tempo)
