# Programa que calcula o seno, cosseno e a tangente de um ângulo.

from math import sin, cos, tan, degrees

angle = float(input("Digite o angulo: "))
print(f'O angulo em seno: {degrees(sin(angle))} em cosseno: {degrees(cos(angle))} e a tangente: {degrees(tan(angle))}')
