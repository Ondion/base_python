# Programa que gera a tabuada de um número até x 10.

numero = int(input('Digite um número: '))
# for i in range(0, 11, 1):
#     print(numero,'X', i, '=',numero * i)
    

for i in range(1, 11):
  print(f'{numero} X {i} = {numero * i}')
