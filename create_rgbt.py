import os
from PIL import Image
import numpy as np

rgb_folder = 'rgb'
thermal_folder = 'thermal'
output_folder = 'rgbt'

files = os.listdir(os.path.join(rgb_folder,'images'))

try:
    os.makedirs(os.path.join(output_folder,'images'))
    os.makedirs(os.path.join(output_folder,'labels'))
except:
    pass

id = 1
qnt = len(files)
for i in files:
    print(id,'/',qnt,'-',i)
    r_img = np.array(Image.open(os.path.join(rgb_folder,'images',i)))
    t_img = np.array(Image.open(os.path.join(thermal_folder,'images',i)))
    t_img = t_img[:, :, 0]
    rgbt_img = np.concatenate((r_img,np.expand_dims(t_img,axis=2)),axis=2)
    rgbt_img = Image.fromarray(rgbt_img)
    rgbt_img.save(os.path.join(output_folder,'images',i))
    id=id+1