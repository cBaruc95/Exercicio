#exercício 12 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
import time

valor = float(input('Quanto você ganha por hora? '))
hora = float(input('Quantas horas foram trabalhadas no mês? '))
tot = valor * hora
ir = (11 * tot) / 100
desc = (tot - ir)
inss = (8 * tot) / 100
desc1 = (tot - inss)
sind = (5 * tot) / 100
desc2 = (tot - sind)
descTot = (tot - desc) + (tot - desc1) + (tot - desc2)
liq = tot - descTot

print(f'Você recebeu um valor bruto de: {tot:.2f}!')
print(f'O desconto foi de {tot - desc:.2f} referente ao Imposto de Renda.')
print(f'O desconto foi de {tot - desc1:.2f} referente ao INSS.')
print(f'O desconto foi de {tot - desc2:.2f} referente ao Sindicato.')
print('--------------------------------------------------')
print(f'O valor líquido de seu salário será de: {liq:.2f}.')
time.sleep(15)