import os
import json
from tqdm import tqdm
import shutil

# 分類照片：有無物件句子
def classification_val_object():
    have_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/have_keyword_picture_num'
    dont_have_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/dont_have_keyword_picture_num'
    val_name_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/val2014_name.txt'
    save_path_have = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/have_picture_name'
    save_path_dont_have = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/dont_have_picture_name'
    image_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/val2014/'
    image_have_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/have_object/'
    image_dont_have_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/dont_have_object/'

    fp_have = open(have_path, 'r')
    fp_dont_have = open(dont_have_path, 'r')
    fp_val_name = open(val_name_path, 'r')
    
    image_name = []
    # 讀取文件 轉為list
    for i in fp_val_name:
        image_name.append(i.replace('\n',''))
        
    have = fp_have.readline().replace('[', '').replace(']', '').split(',')
    dont_have = fp_dont_have.readline().replace('[', '').replace(']', '').split(',')
    for i in range(len(have)):
        have[i] = int(have[i])
    for i in range(len(dont_have)):
        dont_have[i] = int(dont_have[i])
    

    for dirPath, dirNames, fileNames in os.walk(image_path):
        allfile = len(fileNames)
    
    have_num = 0
    dont_have_num = 0
    # 分類照片
    for i in tqdm(range(allfile)):
        if i in have:
            path = image_path + image_name[i]
            copy_path = image_have_path + image_name[i]
            have_num += 1
        if i in dont_have:
            path = image_path + image_name[i]
            copy_path = image_dont_have_path + image_name[i]
            dont_have_num += 1

        shutil.copyfile(path, copy_path)
     
    print('have:', have_num)
    print("don't have". dont_have_num)


# 找出句子有關鍵字的
def find_val_object():
    # 得到有object關鍵字的val照片有哪些
    #=============================================================================================================
    val_data_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/val2014_sentence.txt'

    fp = open(val_data_path, 'r')
    root = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/val2014/'
    allfile = 0
    for dirPath, dirNames, fileNames in os.walk(root):
        allfile = len(fileNames)

    true_sentence = [[] for _ in range(allfile)]
    true_sentence_str = fp.readline().replace('[[[','[[').replace(']]]',']]').split('[[')[1:]

    for i in range(len(true_sentence_str)):   
        true_sentence_str[i] = true_sentence_str[i].split(', [')
        for j in range(len(true_sentence_str[i])):
            true_sentence_str[i][j] = true_sentence_str[i][j].replace('[','').replace(']','').split(',')

    for i in range(len(true_sentence_str)):
            long_tmp_list = []
            for j in range(len(true_sentence_str[i])):
                tmp_list = []
                for k in range(len(true_sentence_str[i][j])):
                    if true_sentence_str[i][j][k] != ' ':
                        tmp_list.append(int(true_sentence_str[i][j][k]))

                long_tmp_list.append(tmp_list)
            true_sentence[i] = long_tmp_list


    importent_word_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/coco_object_list.txt'
    importent_word = open(importent_word_path, 'r')

    #把讀進來的檔案轉成list型態 並將內容值轉為int數字
    for i in importent_word:
        importent_word_list = i.replace('[','').replace(']','').split(',')
    for i, num in zip(importent_word_list, range(len(importent_word_list))):
        importent_word_list[num] = int(i)

    have_key_word_list = []
    have_key_word = 0
    have_key_word_switch = False

    for i in range(len(true_sentence)):
        have_key_word_switch = False
        for j in range(len(true_sentence[i])):
            #print(true_sentence[i][j])
            #input("?")
            for k in true_sentence[i][j]:
                #print(k)
                if k in importent_word_list:
                    have_key_word_switch = True
                    have_key_word += 1
                    have_key_word_list.append(i)
                    #input("???")
                    break
            if have_key_word_switch:
                break

    fp_save = open('/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/have_keyword_num', 'w')
    fp_save.write(str(have_key_word_list))
    fp_save.close()
    print(have_key_word)
    print(len(have_key_word_list))
    print('=====')
    dont_have_key_word_list = []
    for i in range(allfile):
        if i in have_key_word_list:
            pass使用
        else:
            dont_have_key_word_list.append(i)

    fp_save = open('/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/dont_have_keyword_picture_num', 'w')
    fp_save.write(str(dont_have_key_word_list))
    fp_save.close()
    print(len(dont_have_key_word_list))
    print(len(have_key_word_list) + len(dont_have_key_word_list))
    #============================================================================================================

def image_find_info():
    have_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/have_keyword_picture_num'
    dont_have_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/dont_have_keyword_picture_num'
    true_sentence_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/val2014_sentence.txt'
    org_json = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/val2014.json'
    root = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/val2014/'
    allfile = 0
    for dirPath, dirNames, fileNames in os.walk(root):
        allfile = len(fileNames)
    true_sentence = [[] for _ in range(allfile)]
    with open(org_json, 'r') as j:
        org_json_info = json.load(j)
    # 開啟正確答案 轉換成list
    # =======================================
    fp_sentence = open(true_sentence_path, 'r')
    true_sentence_str = fp_sentence.readline().replace('[[[','[[').replace(']]]',']]').split('[[')[1:]
    fp_sentence.close()

    for i in range(len(true_sentence_str)):   
        true_sentence_str[i] = true_sentence_str[i].split(', [')
        for j in range(len(true_sentence_str[i])):
            true_sentence_str[i][j] = true_sentence_str[i][j].replace('[','').replace(']','').split(',')
    
    for i in range(len(true_sentence_str)):
        long_tmp_list = []
        for j in range(len(true_sentence_str[i])):
            tmp_list = []
            for k in range(len(true_sentence_str[i][j])):
                if true_sentence_str[i][j][k] != ' ':
                    tmp_list.append(int(true_sentence_str[i][j][k]))
            long_tmp_list.append(tmp_list)
        true_sentence[i] = long_tmp_list           
    # =======================================

    # 讀入已分類後的圖片編號
    # =======================================
    fp_have = open(have_path, 'r')
    fp_dont_have = open(dont_have_path, 'r')
    have = fp_have.readline().replace('[', '').replace(']', '').split(',')
    dont_have = fp_dont_have.readline().replace('[', '').replace(']', '').split(',')
    
    for i in range(len(have)):
        have[i] = int(have[i])
    for i in range(len(dont_have)):
        dont_have[i] = int(dont_have[i])
    # =======================================
    have_sentence_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/have_keyword_sentence'
    dont_have_sentence_path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/dont_have_keyword_sentence'
    # 將句子分類
    # =======================================
    have_true_sentence = []
    dont_have_true_sentence = []
    have_name = open('/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/have_image_name.txt', 'w')
    dont_have_name = open('/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/dont_have_image_name.txt', 'w')
    have_num = 0
    dont_have_num = 0
    for i in tqdm(range(allfile)):
        if i in have:
            have_true_sentence.append(true_sentence[i])
            have_name.write(org_json_info[i]["filename"] + '\n')
            have_num += 1
        if i in dont_have:
            dont_have_true_sentence.append(true_sentence[i])
            dont_have_name.write(org_json_info[i]["filename"] + '\n')
            dont_have_num += 1
    # =======================================

    #儲存
    fp = open(have_sentence_path, 'w')
    fp.write(str(have_true_sentence))
    fp.close()

    fp = open(dont_have_sentence_path, 'w')
    fp.write(str(dont_have_true_sentence))
    fp.close()

    print('have:' + str(have_num))
    print("don't have:" + str(dont_have_num))


if __name__ == '__main__':
    switch = input("輸入1使用找出object的句子，輸入2分類有無物件的圖片名稱，輸入3用圖片找出圖片json資訊：")
    if switch == '1':
        find_val_object()
    elif switch == '2':
        classification_val_object()
    elif switch == '3':
        image_find_info()