#取得cocodataset 中 caption 中 wordmap 的類別的字的編號
import os
import json

object_file_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/coco_object'
word_map_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/WORDMAP_coco_5_cap_per_img_5_min_word_freq.json'
save_file_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/coco_object_list.txt'

object_file = open(object_file_path, 'r')

with open(word_map_path ,"r") as f:
    word_map = json.load(f)


def find_index(word):
    try:
        return int(word_map[word.replace('\n','')])
    except:
        return -999

word_index_list = []
for word in object_file:
    search = find_index(word)
    if search != -999:
        word_index_list.append(search)
    

object_file.close()

save_file = open(save_file_path, 'w')
save_file.write(str(word_index_list))
save_file.close()

print('finish !')