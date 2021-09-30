#exercício 5 - Faça um Programa que converta metros para centímetros
import time

metros = float(input('Quantos metros, separados por ponto, precisam ser convertidos para CM? '))
cent = metros * 100

print(f'A conversão de metros para centimetros é de: {cent:.2f}cm')
time.sleep(10)

