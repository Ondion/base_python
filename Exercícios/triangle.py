# Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo formado ou "não é triangulo", caso não seja possível formar um triângulo.

lados = []

while len(lados) != 3:
  lados.append(int(input('Digite um lado do triangulo: ')))
  
def is_triangle(sides):
  return True if lados[0] + lados[1] > lados[2] and lados[0] + lados[2] > lados[1] and lados[1] + lados[2] > lados[0] else False

def type_of_triangle(test, sides):
  if not test:
    return 'não é um triângulo...'
  if sides[0] == sides[1] == sides[2]:
    return 'Triângulo Equilátero'
  if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
    return 'Triângulo Isósceles'
  if sides[0] != sides[1] != sides[2]:
    return 'Triângulo Escaleno'

print(type_of_triangle(is_triangle(lados), lados))
