#exercício 1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
import math
import time

print('Olá mundo!')

#exercício 2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]
num = int(input('Escolha um número: '))
print('O número escolhido foi:', num)
print('--------------------------------------------------')
#exercício 3 - Faça um Programa que peça dois números e imprima a soma
num1 = int(input('Escolha um número para soma: '))
num2 = int(input('Escolha outro número para soma: '))
res = num1 + num2
print(f'A soma entre {num1} e {num2} é igual a: {res}')
print('--------------------------------------------------')
#exercício 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sua segunda nota? '))
n3 = float(input('Qual foi sua terceira nota? '))
n4 = float(input('Qual foi sua quarta nota? '))
n5 = 4
media = (n1 + n2 + n3 + n4) / n5
print('Sua média foi de:', media)
if media >= 7:
    print('Parabéns, você está acima da média!')
else:
    print('Você está abaixo da média, estude mais!')
print('--------------------------------------------------')
#exercício 5 - Faça um Programa que converta metros para centímetros
metros = float(input('Quantos metros, separados por ponto, precisam ser convertidos para CM? '))
cent = metros * 100
print(f'A conversão de metros para centimetros é de: {cent:.2f}cm')
print('--------------------------------------------------')
#exercício 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input('Qual o raio do circulo? '))
formula = math.pi * (raio**2)

print(f'A área do circulo será de: {formula:.2f}')
print('--------------------------------------------------')
#exercício 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input('Qual o valor de um dos lados do quadrado? '))
form = lado**2

print(f'O valor de área é: {form}, e seu dobro é {form * 2}')
print('--------------------------------------------------')
#exercício 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
salario = float(input('Quanto você ganha por hora? '))
horas = float(input('Quantas horas você trabalhou no mês? '))
res = salario * horas

print(f'Você irá receber R${res:.2f}!')
print('--------------------------------------------------')
#exercício 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
temp = float(input('Qual a temperatura em Fahrenheit? '))
conv = (temp - 32) / 1.8

print(f'A temperatura em Celsius é de: {conv:.2f}')
print('--------------------------------------------------')
#exercício 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
temp1 = float(input('Qual a temperatura em Celsius? '))
conv1 = (temp1 * 1.8) + 32

print(f'A temperatura em Fahrenheit é de: {conv1:.2f}')
print('--------------------------------------------------')
#exercício 11 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input('Qual seu altura? '))
form3 = (72.7 * altura) - 58

print(f'Seu peso ideal é de: {form3:.2f}')
print('--------------------------------------------------')
#exercício 12 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
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











