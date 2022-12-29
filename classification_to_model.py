import deeplabcut
import os
import cv2 as cv
import numpy as np
import json

data_path = "C:\\Users\\Archit\\Documents\\Fall_22\\CSCI5561\\final_proj\\cropped_val"
import h5py

apes = ["gibbon","siamang","bonobo","orangutan","chimpanzee","gorilla"]

#black out the rest of the image
def crop_image(img, x1, y1, width, height):
    crop_img = img.copy()
    # crop_img[y1:y1+height, x1:x1+width] = 0
    crop_img[y1:y1+height, 0:x1] = 0
    crop_img[y1:y1+height, x1+width:] = 0
    crop_img[0:y1, 0:] = 0
    crop_img[y1+height:, 0:] = 0
    return crop_img

#load test_json
with open('val_annotation_answer.json','r') as f:
    data = json.load(f)
    for i in data['data']:
        if i['species'].lower() in apes:
            img = cv.imread('validation/val/'+i['file'])
            x1 = i['bbox'][0]
            y1 = i['bbox'][1]
            width = i['bbox'][2]
            height = i['bbox'][3]
            crop_img = crop_image(img, x1, y1, width, height)
            cv.imwrite('cropped_val/'+i['file'], crop_img)
f.close()
    
config_path =os.path.join(os.path.join(os.getcwd(), 'working_dir'),'openmonkeychallenge_train_apes-group-2022-12-11','config.yaml')

deeplabcut.analyze_videos(config_path, ['C:\\Users\\Archit\\Documents\\Fall_22\\CSCI5561\\final_proj\\cropped_val'], videotype='.jpg', gputouse=0, save_as_csv=True)

with open('val_annotation_answer.json','r+') as f:
    data = json.load(f)
    for j in os.listdir(data_path):
        for i in data['data']:
            if i['file'] == j:
                h5file = h5py.File(os.path.join(data_path, j[:-4]+'DLC_resnet50_openmonkeychallenge_train_apesDec11shuffle1_650000.h5'), 'r')
                coord_table = h5file['df_with_missing']['table'][0][1]
                
                coord_table = np.array(coord_table,dtype=int).reshape(51,)
                # print(coord_table)
                data_in = [coord_table[0], coord_table[1], coord_table[3], coord_table[4], coord_table[6], coord_table[7],
                    coord_table[9], coord_table[10], coord_table[12], coord_table[13], coord_table[15], coord_table[16], coord_table[18],
                    coord_table[19], coord_table[21], coord_table[22], coord_table[24], coord_table[25], coord_table[27], coord_table[28],
                    coord_table[30], coord_table[31], coord_table[33], coord_table[34], coord_table[36], coord_table[37], coord_table[39], coord_table[40],
                    coord_table[42], coord_table[43], coord_table[45], coord_table[46], coord_table[48], coord_table[49]]
                # print(data_in)
                # print(i['landmarks'])
                for k in data_in:
                    i['landmarks'].append(int(k))
                print (i['landmarks'])
                h5file.close()
    f.seek(0)
    json.dump(data, f)
    f.truncate()
f.close() 

# RUN COMPARE_TO_TRUTH ONCE THIS STEP IS COMPLETE