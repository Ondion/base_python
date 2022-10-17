# Faça um programa que, dado um valor n qualquer, tal que n > 1, imprima na tela um triângulo retângulo com n asteriscos de base.

numero = int(input('Numero de *: '))

for x in range(0, numero + 1):
  print(f'{" " * (numero - x)} {"*" * (x + x -1)}')

print(f'{" " * (numero -1)}| |{" " * (numero -1)}')
print(f'{"_" * (numero -1)}|_|{"_" * (numero -1)}')
