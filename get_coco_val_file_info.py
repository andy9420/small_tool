#取得cocodataset 中 caption 中 wordmap 的類別的字的編號
import os
import json
from tqdm import tqdm

#object_file_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/coco_object'zz
# word map 路徑
word_map_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/WORDMAP_coco_5_cap_per_img_5_min_word_freq.json'
# 全部資料得json檔路徑
coco_dataset_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/dataset_coco.json'
# 要儲存 存放要測試檔案的資訊的json檔 檔案位置
save_file_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/val2014.json'
# 儲存只有 要測試的檔案名稱 檔案位置
save_filename_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/val2014_name.txt'
# 儲存只有 要測試的句子 檔案位置
save_sentence_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/val2014_sentence.txt'
#object_file = open(object_file_path, 'r')

# 讀取全部資料及的資訊
with open(coco_dataset_path ,"r") as f:
# 讀取 word map 資訊
    coco_dataset = json.load(f)

with open(word_map_path ,"r") as f:
    word_map = json.load(f)

val2014 = []
val_name = []
val_sentence = []



# 開啟要儲存檔案的位置
fp_filename = open(save_filename_path, "w")
fp_sentence = open(save_sentence_path, "w")

# 有存放全部要測試的檔案的資料夾 的路徑
for dirPath, dirNames, fileNames in os.walk('/media/cvlab/5CA28BFDA28BDA42/coco_dataset/val2014'):
    counr_all_file = len(fileNames)

# 建立二維空陣列
true_sentence = [[] for _ in range(counr_all_file)]


num =  0 
# 找到 json 檔中 路徑是val2014的檔案 把他的資料取出 
for i in tqdm(range(len(coco_dataset['images']))):
    if coco_dataset['images'][i]['filepath'] == 'val2014':
        num += 1
        val2014.append(coco_dataset['images'][i])
        fp_filename.write(coco_dataset['images'][i]['filename'])
        fp_filename.write('\n')

        
        # 依據句子數量設定
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


