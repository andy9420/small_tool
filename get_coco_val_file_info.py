#取得cocodataset 中 caption 中 wordmap 的類別的字的編號
import os
import json
from tqdm import tqdm

#object_file_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/coco_object'
word_map_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/WORDMAP_coco_5_cap_per_img_5_min_word_freq.json'
coco_dataset_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/dataset_coco.json'
save_file_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/val2014.json'
save_filename_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/val2014_name.txt'
save_sentence_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/val2014_sentence.txt'
#object_file = open(object_file_path, 'r')

with open(coco_dataset_path ,"r") as f:
    coco_dataset = json.load(f)

with open(word_map_path ,"r") as f:
    word_map = json.load(f)

val2014 = []
val_name = []
val_sentence = []



fp_filename = open(save_filename_path, "w")
fp_sentence = open(save_sentence_path, "w")

for dirPath, dirNames, fileNames in os.walk('/media/cvlab/5CA28BFDA28BDA42/coco_dataset/val2014'):
    counr_all_file = len(fileNames)

# 建立二維空陣列
true_sentence = [[] for _ in range(counr_all_file)]


num =  0
# 找到路徑是val2014的檔案 把他的資料取出 
for i in tqdm(range(len(coco_dataset['images']))):
    if coco_dataset['images'][i]['filepath'] == 'val2014':
        num += 1
        val2014.append(coco_dataset['images'][i])
        fp_filename.write(coco_dataset['images'][i]['filename'])
        fp_filename.write('\n')

        
        sentence = ['','','','','']
        for number in range(5):
            small_sentence = []
            for s in coco_dataset['images'][i]['sentences'][number]['tokens']:
                try:
                    small_sentence.append(word_map[s])
                except:
                    small_sentence.append(0)
            small_sentence.append(9489)
            #print(small_sentence)
            #input(1)
            sentence[number] = small_sentence
            #print(sentence)
            #input(2)
        true_sentence[i] = sentence
        #print(true_sentence)
        #input(3)
        #val_name.append(coco_dataset['images'][i]['filename'])

fp_sentence.write(str(true_sentence))
test = val2014
'''for dirPath, dirNames, fileNames in os.walk('/media/cvlab/5CA28BFDA28BDA42/coco_dataset/val2014'):
    print(fileNames)
    input()
    #file_num = len(fileNames)
    #for name in range(len(fileNames)):
    #    if fileNames[name] == '''
        

with open(save_file_path,"w") as f:
    json.dump(val2014, f)

'''
with open(save_sentence_path,"w") as f:
    json.dump(true_sentence, f)
'''
print(num)  # val2014 檔案數量40504
print('finish!')

fp_filename.close()
fp_sentence.close()
'''
# 計算檔案數量
num = 0
for dirPath, dirNames, fileNames in os.walk('/media/cvlab/5CA28BFDA28BDA42/coco_dataset/val2014'):
    for f in fileNames:
       num += 1
print(num)
print('finish!')
'''


