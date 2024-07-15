import os
from time import sleep

file = 'metainfo.csv'

def get_folders(file):
    folders = []
    raw = []
    with open(file,'r') as f:
        raw = f.readlines()
    #print(raw[0].replace('\n','')) #TO print HEADER
    for line in raw[1:]:
        if line.replace('\n','').split(';')[1] not in folders:
            folders.append(line.replace('\n','').split(';')[1])

    total_obj = []
    total_rgb = 0
    total_thermal = 0
    for folder in folders:
        img_folder = 0
        obj_thermal = 0
        obj_rgb = 0
        for line in raw:
            if folder in line:
                img_folder = img_folder + 1
                thermal, rgb = line.replace('\n','').split(';')[-2:]
                obj_thermal = obj_thermal + int(thermal)
                obj_rgb = obj_rgb + int(rgb)
                total_rgb = total_rgb + int(rgb)
                total_thermal = total_thermal + int(thermal)
        total_obj.append({
            'folder': folder,
            'images': img_folder,
            'rgb': obj_rgb,
            'thermal': obj_thermal
        })
        print(folder,obj_rgb,obj_thermal)
    print('Full total RGB:',total_rgb)
    print('Full total Thermal:',total_thermal)
    with open('folder_info.csv','w') as f:
        f.write('FOLDER;IMAGES;RGB OBJ['+str(total_rgb)+'];THERMAL OBJ['+str(total_thermal)+']\n')
        for i in total_obj:
            f.write(i['folder']+';'+str(i['images'])+';'+str(i['rgb'])+';'+str(i['thermal'])+'\n')
    
    
    
if __name__ == '__main__':
    get_folders(file)
