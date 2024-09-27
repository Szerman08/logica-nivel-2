# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

d1 = int(input("Quantos anos você tem ? \n"))
d2 = int(input("Quantos meses você tem ? \n"))
d3 = int(input("Quanto dias de vida você tem ? \n"))

r1 = (d1*365) 
r2 = (d2*30)

print (r1 + r2 + d3)
