
#delete images in train_im/train that are not apes based off of train_annotations.json

import json
import os
apes = ["gibbon","siamang","bonobo","orangutan","chimpanzee","gorilla"]

with open('train_annotation.json') as f:
    data = json.load(f)
    for i in data['data']:
        if i['species'].lower() not in apes:
            os.remove('train_im/train/'+i['file'])

