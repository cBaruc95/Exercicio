#exercício 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
import time

salario = float(input('Quanto você ganha por hora? '))
horas = float(input('Quantas horas você trabalhou no mês? '))
res = salario * horas

print(f'Você irá receber R${res:.2f}!')
time.sleep(10)
