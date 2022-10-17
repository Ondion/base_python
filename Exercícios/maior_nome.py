# Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"].

lista_nomes = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]
maior = ''

for nome in lista_nomes:
  maior = nome if len(nome) >= len(maior) else maior

print(maior)
