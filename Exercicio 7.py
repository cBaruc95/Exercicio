#exercício 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
import time

lado = float(input('Qual o valor de um dos lados do quadrado? '))
form = lado**2

print(f'O valor de área é: {form}, e seu dobro é {form * 2}')
time.sleep(10)
