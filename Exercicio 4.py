#exercício 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
import time

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
time.sleep(10)
