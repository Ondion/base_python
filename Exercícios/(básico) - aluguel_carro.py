# Programa que faz o calculo de aluguel entre, Kms rodados x tempo de uso. Valor do dia R$: 60,00, valor do Km R$: 0,15.

tempo = int(input('Quantos dias de uso do carro? '))
kms = int(input('Quantos Kms rodados? '))
print(f'Você rodou {kms}kms e usou o veiculo por {tempo} dias, o valor a pagar é R$:{(tempo * 60) + (kms * 0.15)}')
