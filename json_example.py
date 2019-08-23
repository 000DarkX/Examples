import json

weapons =[ {"name": "Sword", "attack": 5}, {"name": "hammer", "attack":7}]

print(weapons)

# saves weapons array into weapons.json
with open("weapons.json", "w") as f:
    data = json.dumps(weapons)
    f.write(data)

weapons = []

# loads weapons.json into weapons
with open("weapons.json") as f:
    data = f.read()
    weapons = json.loads(data)

print(weapons)