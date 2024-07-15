import os
from PIL import Image
import numpy as np

input_folder = 'depth'
output_folder = 'depth-n'

files = os.listdir(os.path.join(input_folder,'images'))

try:
    os.makedirs(os.path.join(output_folder,'images'))
    os.makedirs(os.path.join(output_folder,'labels'))
except:
    pass

img = np.array(Image.open(os.path.join(input_folder,'images',files[0])))
min = np.min(img)
max = np.max(img)

for i in files:
    img = np.array(Image.open(os.path.join(input_folder,'images',i)))
    if np.min(img) < min:
        min = np.min(img)
    if np.max(img) > max:
        max = np.max(img)

id = 1
qnt = len(files)
for i in files:
    print(id,'/',qnt,'-',i)
    img = np.array(Image.open(os.path.join(input_folder,'images',i)))
    img_n = ((img-min)/(max-min)) * 255
    img_n = img_n.astype('uint8')
    img_n = Image.fromarray(img_n)
    img_n.save(os.path.join(output_folder,'images',i))
    id=id+1