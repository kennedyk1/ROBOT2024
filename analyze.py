import os

file = 'metainfo.csv'

def get_folders(file):
    data = []
    with open(file,'r') as f:
        data = f.readlines()
    print(data)
    
if __name__ == '__main__':
    get_folders(file)