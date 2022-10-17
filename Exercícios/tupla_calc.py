#  Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede (em m²).

parede_m2 = int(input('Tamanho da parede em metros: '))

def wall_calc(wall):
  latas = ((wall / 3) // 18 ) + 1
  return (f'É necessário {latas} lata(s) de tinta', f'O valor total é R$:{latas * 80.00}')

print(wall_calc(parede_m2))
