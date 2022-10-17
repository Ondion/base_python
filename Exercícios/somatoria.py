#  Crie uma função que receba um número inteiro N e retorne o somatório de todos os números de 1 até N.

def somatoria(x):
  result = 0
  for number in range(1, x + 1):
    result = result + number
    print(f'Valor atual result: {result}, Valor atual number: {number}')
  return result

print(somatoria(1000))
