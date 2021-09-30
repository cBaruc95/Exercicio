#exercício 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
import time

temp1 = float(input('Qual a temperatura em Celsius? '))
conv1 = (temp1 * 1.8) + 32

print(f'A temperatura em Fahrenheit é de: {conv1:.2f}')
time.sleep(10)
