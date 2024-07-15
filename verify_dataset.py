import os

with open('metainfo.csv','r') as f:
    raw = f.readlines()

data = []

for line in raw[1:]:
    data.append(line.replace('\n','').split(';')[0])

rgb_img = os.listdir(os.path.join('thermal','images'))
img = []

for i in rgb_img:
    img.append(i.split('.')[0])

for i in data:
    if i not in img:
        print(i)