import os
import shutil

meta_file = 'metainfo.csv'
modalities = ['depth','intensity','rgb','thermal']
#DAYS 29 and 8
test = ['2024-04-29-11-09-38_bag_DEEC_4','2024-04-29-14-45-11_bag_DEI_4','2024-04-29-14-57-35_bag_DEEC_4','2024-05-08-15-07-59_bag_DEI_4','2024-05-08-15-18-54_bag_DEEC_4']

#DAYS 16, 7 and 9
train = ['2024-05-07-13-42-00_bag_DEEC_4','2024-05-07-13-54-12_bag_DEEC_2','2024-05-07-14-05-58_bag_DEEC_3','2024-05-07-14-13-29_bag_DEEC_4','2024-05-09-09-59-39_bag_DEI_2','2024-05-09-10-07-45_bag_DEI_4','2024-05-09-10-16-08_bag_DEEC_4','2024-05-09-10-49-49_bag_DEEC_2','2024-05-09-10-56-15_bag_DEI_2','2024-05-09-11-04-02_bag_DEI_2','2024-05-09-11-16-35_bag_DEEC_4','2024-05-09-15-23-58_bag_DEEC_2','2024-05-09-15-24-46_bag_DEEC_2','2024-05-09-15-26-04_bag_DEEC_2','2024-05-09-15-27-02_bag_DEEC_2','2024-05-09-15-30-32_bag_DEI_2','2024-05-09-15-35-55_bag_DEI_4','2024-05-09-15-41-57_bag_DEEC_4','2024-05-09-15-48-42_bag_DEEC_2','2024-05-09-15-53-32_bag_DEEC_2','2024-05-09-15-53-49_bag_DEEC_2','2024-05-16-10-38-51_bag_DEEC_2','2024-05-16-10-40-09_bag_DEEC_2','2024-05-16-10-41-18_bag_DEEC_2','2024-05-16-10-49-46_bag_DEEC_4','2024-05-16-10-57-44_bag_DEI_4','2024-05-16-12-31-33_bag_DEEC_2','2024-05-16-12-33-00_bag_DEEC_2','2024-05-16-12-34-46_bag_DEEC_2','2024-05-16-12-37-44_bag_DEI_2','2024-05-16-12-38-27_bag_DEI_2','2024-05-16-12-39-13_bag_DEI_2','2024-05-16-12-39-56_bag_DEI_2','2024-05-16-12-41-15_bag_DEI_2','2024-05-16-12-43-58_bag_DEI_2','2024-05-16-12-46-51_bag_DEI_2','2024-05-16-12-49-36_bag_DEI_2','2024-05-16-12-51-40_bag_DEI_2','2024-05-16-12-53-40_bag_DEI_2','2024-05-16-12-55-24_bag_DEI_2','2024-05-16-12-59-29_bag_DEEC_2']

all_files = []
test_files = []
train_files = []

with open(meta_file,'r') as f:
    raw = f.readlines()

for line in raw[1:]:
    all_files.append(line.split(';')[0])

for modality in modalities:
    try:
        os.makedirs(os.path.join('train',modality,'images'))
        os.makedirs(os.path.join('train',modality,'labels'))
        os.makedirs(os.path.join('test',modality,'images'))
        os.makedirs(os.path.join('test',modality,'labels'))
    except:
        pass

id = 1
for line in raw[1:]:
    print('Copying files id',id)
    file, bag = line.split(';')[0:2]
    if bag in test:
        for modality in modalities:
            #TO COPY IMAGES
            src = os.path.join(modality,'images',file+'.png')
            dst = os.path.join('test',modality,'images')
            shutil.copy(src,dst)
            #TO COPY LABELS
            src = os.path.join(modality,'labels',file+'.txt')
            dst = os.path.join('test',modality,'labels')
            shutil.copy(src,dst)
            
    if bag in train:
        for modality in modalities:
            #TO COPY IMAGES
            src = os.path.join(modality,'images',file+'.png')
            dst = os.path.join('train',modality,'images')
            shutil.copy(src,dst)
            #TO COPY LABELS
            src = os.path.join(modality,'labels',file+'.txt')
            dst = os.path.join('train',modality,'labels')
            shutil.copy(src,dst)
    id = id+1