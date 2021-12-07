# Programa que realiza sorteiro entre quatro strings e as imprime na ordem do sorteio.

from random import shuffle

nome_1 = str(input("primeira string: "))
nome_2 = str(input("segunda string: "))
nome_3 = str(input("terceira string: "))
nome_4 = str(input("quarta string: "))
sorteio = [nome_1, nome_2, nome_3, nome_4]
shuffle(sorteio)
print(sorteio)
