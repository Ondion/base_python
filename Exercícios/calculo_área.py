# Programa para calcular a quantidade de tinta necessária para pintar uma parede, tendo em consideração que cada litro de tinta pinta uma área de 2m quadrados.

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
print(f'A área da parede é: {altura*largura}, por esse motivo, serão necessários {(altura+largura)/2} litros de tinta para a pintura.')
