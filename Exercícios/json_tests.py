import json

with open('../data/pokemon.json', 'r') as file:
  charizard = json.load(file)


print(charizard['abilities'])
