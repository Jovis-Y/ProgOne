""""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    · salário bruto.
    · quanto pagou ao INSS.
    · quanto pagou ao sindicato.
    · o salário líquido.
    · calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$ 
- IR (11%) : R$ 
- INSS (8%) : R$ 
- Sindicato ( 5%) : R$ 
= Salário Liquido : R$ 
Obs.: Salário Bruto - Descontos = Salário Líquido. 
"""

ganho = float(input("Quanto você recebe por hora: "))
horas = float(input("Quantas horas você trabalha por mês: "))
salarioBruto = horas * ganho
descontoINSS = salarioBruto * 0.08
descontoIR = salarioBruto * 0.11
descontoSindi = salarioBruto * 0.05
salarioLiquido = salarioBruto * 0.76

print("Salário bruto:", salarioBruto)
print("Desconto INSS:", descontoINSS)
print("Desconto Sindicato:", descontoSindi)
print("Desconto Imposto de Renda:", descontoIR)
print("Salário Líquido:", salarioLiquido)
