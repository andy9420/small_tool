import os
from PIL import Image

path = '/home/cvlab/ContourNet/datasets/ic15/my_data'

i = 0

#多資料夾
'''
for fname in os.listdir(path):
    fdir_root = os.path.join(path,fname)
    for fdir in os.listdir(fdir_root):
        new_fname = str(i).zfill(7) + fdir[-4:]
        os.rename(os.path.join(fdir_root,fdir), os.path.join(fdir_root,new_fname))
        i += 1
'''

#單資料夾
for fname in os.listdir(path):
    new_fname = str(i).zfill(7) + fname[-4:]
    os.rename(os.path.join(path,fname), os.path.join(path,new_fname))
    i += 1


'''
for fname in os.listdir(path):
    if fname[-3:] == 'png' or fname[-3:] == 'PNG':
        print(fname)
        im1 = Image.open(os.path.join(path,fname))
        new_fname = fname[:-4] + '.jpg'
        im1.save(os.path.join(path,new_fname))
'''