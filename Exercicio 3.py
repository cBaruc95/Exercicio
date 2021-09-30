#exercício 3 - Faça um Programa que peça dois números e imprima a soma
import time

num1 = int(input('Escolha um número para soma: '))
num2 = int(input('Escolha outro número para soma: '))
res = num1 + num2

print(f'A soma entre {num1} e {num2} é igual a: {res}')
time.sleep(10)