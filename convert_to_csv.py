import json
import os
line1= 'scorer,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group,group\n'
line2 = 'bodyparts,Nose,Nose,Left_eye,Left_eye,Right_eye,Right_eye,Head,Head,Neck,Neck,Left_shoulder,Left_shoulder,Left_elbow,Left_elbow,Left_wrist,Left_wrist,Right_shoulder,Right_shoulder,Right_elbow,Right_elbow,Right_wrist,Right_wrist,Hip,Hip,Left_knee,Left_knee,Left_ankle,Left_ankle,Right_knee,Right_knee,Right_ankle,Right_ankle,Tail,Tail\n'
line3 = 'coords,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y\n'
directory = os.path.join(os.getcwd(),'working_dir','openmonkeychallenge_train_apes-group-2022-12-11','labeled-data')
with open('train_annotation.json') as f:
    data = json.load(f)

    #loop through json file
    for i in data['data']:
        if os.path.exists(os.path.join(directory,i['file'][:-4])):
            #print(os.path.join(directory,i['file'][:-4]))
            with open(os.path.join(directory,i['file'][:-4],'CollectedData_group.csv'), 'w') as csv:
                csv.write(line1)
                csv.write(line2)
                csv.write(line3)
                csv.write(str(os.path.join('labeled-data',i['file'][:-4],'img0.png')) + ',')
                for j in i['landmarks']:
                    #write to csv file remopving the last comma
                    if j == i['landmarks'][-1]:
                        csv.write(str(j))
                    else:
                        csv.write(str(j)+',')
                
                csv.write('\n')