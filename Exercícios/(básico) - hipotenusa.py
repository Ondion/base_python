# Programa que calcula a hipotenusa de um triângulo retangulo, com o resultado em um número inteiro.

from math import hypot, trunc

cateto = float(input('Digite o cateto: '))
cateto_oposto = float(input('Digite o cateto oposto: '))

print(f'A hipotenusa do triângulo é {trunc(hypot(cateto, cateto_oposto))}')
