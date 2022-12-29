import json
import numpy as np

# Load the annotation file
threshold = 0.5
ki = 0.2
def OKS_sigma(OKS,threshold):
    if OKS>= threshold:
        return 1
    else:
        return 0

def sigma(input,threshold):
    if input < threshold:
        return 1
    else:
        return 0

with open('val_annotation.json', 'r') as f:
    data = json.load(f)
    with open('val_annotation_answer.json', 'r') as f2:
        data_answers = json.load(f2)
        J = 0
        mean_joint_error = [0 for i in range(17)]
        sigma_tot = 0
        AP_tot = 0
        for i in data_answers['data']:
            if len(i['landmarks']) == 0:
                continue
            for j in data['data']:
                if i['file'] == j['file']:
                    mean_counter = 0
                    for k in range(0,len(i['landmarks']),2):
                        # print(i['landmarks'][k], i['landmarks'][k+1], j['landmarks'][k], j['landmarks'][k+1])
                        W = j['bbox'][2]
                        norm = np.linalg.norm(np.array([int(i['landmarks'][k]),int(i['landmarks'][k+1])]) - np.array([int(j['landmarks'][k]), int(j['landmarks'][k+1])]))
                        OKS = np.exp(-1*(norm**2)/(2*(W**2)*(ki**2)))
                        mean_joint_error[mean_counter] += norm/W
                        sigma_tot += sigma(norm/W,threshold)
                        AP_tot += OKS_sigma(OKS,threshold)
                        mean_counter += 1
                    J += 1
        for i in range(len(mean_joint_error)):
            mean_joint_error[i] = mean_joint_error[i]/J

        MPJPE = sum(mean_joint_error)/len(mean_joint_error)
        PCK = (1/(17*J))*sigma_tot
        AP = (1/(17*J))*AP_tot

print('AVERAGE MPJPE: ', MPJPE)
print('MPJPE per joint: ')
for i in range(len(mean_joint_error)):
    print(mean_joint_error[i])
print('PCK: ', PCK)
print('AP: ', AP)
                        
