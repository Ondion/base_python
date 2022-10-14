# Programa que calcula o seno, cosseno e a tangente de um ângulo.

from math import sin, cos, tan, radians

angle = float(input("Digite o angulo: "))
print(f'O angulo em seno: {sin(radians(angle))} em cosseno: {cos(radians(angle))} e a tangente: {tan(radians(angle))}')
