#exercício 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
import time

temp = float(input('Qual a temperatura em Fahrenheit? '))
conv = (temp - 32) / 1.8

print(f'A temperatura em Celsius é de: {conv:.2f}')
time.sleep(10)
