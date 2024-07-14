import os
from time import sleep

folders = ['rgb','thermal']

def count_bbox(labels):
    tmp = []
    for label in labels:
        if(label.replace('\n','') != ''):
            tmp.append(label.replace('\n',''))
    return len(tmp)
    
def analyze(folders):
    dataset_info = []
    for folder in folders:
        folder_info = []
        files = os.listdir(os.path.join(folder,'labels'))
        for file in files:
            data = ""
            with open(os.path.join(folder,'labels',file),'r') as f:
                data = f.readlines()
            bboxes = count_bbox(data)
            folder_info.append(
                {
                    'file': file,
                    'bboxes': bboxes
                }
            )
        dataset_info.append({
            'folder': folder,
            'data': folder_info
        })
    return dataset_info

def export_csv(filename, data):
    for folder in data:
        with open(filename+'_'+folder['folder']+'.csv', 'w') as f:
            f.write('file;objects\n')
            for info in folder['data']:
                f.write(info['file']+';'+str(info['bboxes'])+'\n')
    
if __name__ == '__main__':
    data = analyze(folders)
    export_csv('dataset',data)
