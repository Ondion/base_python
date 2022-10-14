# Programa que calcula a média de valores, de forma indefinida.

lista = []

while(True):
  lista.append(int(input('valor: ')))
  if input('sair? '):
    break

print(f'média: {sum(lista) / len(lista)}')