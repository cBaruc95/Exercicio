#exercício 11 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58
import time

altura = float(input('Qual seu altura? '))
form3 = (72.7 * altura) - 58

print(f'Seu peso ideal é de: {form3:.2f}')
time.sleep(10)
