# Programa para testar uma string ou caráter, com os diversos métodos disponiveis.

valor = str(input('Entre com a string para teste: '))

print(valor, 'é numérico?', valor.isnumeric())
print(valor, 'é alphanumérico?', valor.isalnum())
print(valor, 'é ascii?', valor.isascii())
print(valor, 'é decimal?', valor.isdecimal())
print(valor, 'é um digito?', valor.isdigit())
print(valor, 'é letra?', valor.isalpha())
print(valor, 'é identificador?', valor.isidentifier())
print(valor, 'é minúsculo?', valor.islower())
print(valor, 'é imprimivel?', valor.isprintable())
print(valor, 'é espaço?', valor.isspace())
print(valor, 'é titulo?', valor.istitle())
print(valor, 'é maiúscula?', valor.isupper())
