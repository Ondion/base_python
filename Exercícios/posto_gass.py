#   Álcool:
#     - Até 20 litros, desconto de 3% por litro;
#     - Acima de 20 litros, desconto de 5% por litro.
#   Gasolina:
#     - Até 20 litros, desconto de 4% por litro;
#     - Acima de 20 litros, desconto de 6% por litro.
# Escreva uma função que receba o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A - álcool, G - gasolina), e retorne o valor a ser pago pelo cliente, sabendo-se que o preço do litro da gasolina é R$ 2,50, e o preço do litro do álcool é R$ 1,90.

litros = float(input('Litros: '))
tipo = input('A ou G: ').lower()

def calc(type, amount):
  if type == 'g':
    return f'Valor a ser pago: R$ {(amount * 2.5) * 0.97}' if amount <= 20 else f'Valor a ser pago: R$ {(amount * 2.5) * 0.95}'
  if type == 'a':
    return f'Valor a ser pago: R$ {(amount * 1.9) * 0.97}' if amount <= 20 else f'Valor a ser pago: R$ {(amount * 1.9) * 0.95}'

print(calc(tipo, litros))
