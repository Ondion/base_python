# Programa que sorteia uma string entre quatro delas.

from random import randint

nome_1 = input("primeira string: ")
nome_2 = input("segunda string: ")
nome_3 = input("terceira string: ")
nome_4 = input("quarta string: ")
sorteio = randint(1, 4)

if sorteio == 1:
    print(nome_1)
if sorteio == 2:
    print(nome_2)
if sorteio == 3:
    print(nome_3)
if sorteio == 4:
    print(nome_4)
