import json
species = []
with open('val_annotation.json') as f:
    data = json.load(f)
    for i in data['data']:
        if i['species'] not in species:
            species.append(i['species'])
print(species)
print(len(species))