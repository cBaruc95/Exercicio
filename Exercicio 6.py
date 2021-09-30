#exercício 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
import time

raio = float(input('Qual o raio do circulo? '))
formula = math.pi * (raio**2)

print(f'A área do circulo será de: {formula:.2f}')
time.sleep(10)
