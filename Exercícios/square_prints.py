# Programa que, dado um valor n qualquer, tal que n > 1, imprima na tela um quadrado feito de asteriscos de lado de tamanho.

n = int(input('Valor dos lados do quadrado: '))

for x in range(0, n):
  print('*' * n)