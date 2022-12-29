import json

with open('val_annotation_answer.json', 'r+') as f:
    data = json.load(f)
    for i in data['data']:
        i['landmarks'] = []
    f.seek(0)
    json.dump(data, f)
    f.truncate()
f.close()

