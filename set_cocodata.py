import json
import os

'''
{"images": [{"filepath": "val2014", "sentids": [770337, 771687, 772707, 776154, 781998], "filename": "COCO_val2014_000000391895.jpg", 
"imgid": 0, "split": "test", "sentences": [{"tokens": ["a", "man", "with", "a", "red", "helmet", "on", "a", "small", "moped", "on", "a", "dirt", "road"], 
"raw": "A man with a red helmet on a small moped on a dirt road. ", "imgid": 0, "sentid": 770337}, 
{"tokens": ["man", "riding", "a", "motor", "bike", "on", "a", "dirt", "road", "on", "the", "countryside"], 
"raw": "Man riding a motor bike on a dirt road on the countryside.", "imgid": 0, "sentid": 771687}, 
{"tokens": ["a", "man", "riding", "on", "the", "back", "of", "a", "motorcycle"], 
"raw": "A man riding on the back of a motorcycle.", "imgid": 0, "sentid": 772707}, 
{"tokens": ["a", "dirt", "path", "with", "a", "young", "person", "on", "a", "motor", "bike", "rests", "to", "the", "foreground", "of", "a", "verdant", "area", "with", "a", "bridge", "and", "a", "background", "of", "cloud", "wreathed", "mountains"], 
"raw": "A dirt path with a young person on a motor bike rests to the foreground of a verdant area with a bridge and a background of cloud-wreathed mountains. ", "imgid": 0, "sentid": 776154}, 
{"tokens": ["a", "man", "in", "a", "red", "shirt", "and", "a", "red", "hat", "is", "on", "a", "motorcycle", "on", "a", "hill", "side"], 
"raw": "A man in a red shirt and a red hat is on a motorcycle on a hill side.", "imgid": 0, "sentid": 781998}], "cocoid": 391895}], "dataset": "coco"}
'''
root = input('Root path:')
json_path = input('save path and file name:')
sentence_num = int(input('Enter a picture sentence number:'))

my_json = {"images": [], "dataset":"coco"}
#image in json["images"]
image = {"filepath": "","sentids": [], "filename": "","imgid": 0,"split": "","sentences":[], "cocoid":0}
#sentence in image["sentences"]
sentence = {"tokens":"" ,"raw": "","imgid": 0, "sentid": 0}

images_json = []

info = []

#檔案輸入
'''
fp = open('/home/cvlab/pyTorch_Image_Captioning/sentence','r')
fp_sentence = []
for i in fp:
    fp_sentence.append(i.replace('\n',''))
fp.close()
'''

sentence_id = 0

dataset_dir = ['train2014','val2014','test2014']

img_id = 0
sent_id = 800000
for d in dataset_dir:
    path = os.path.join(root, d) 
    for dirPath, dirNames, fileNames in os.walk(path):
        sentids = []
        for dataset_file in fileNames:
            print(path)
            print(dataset_file)
            print(dataset_file[-13:-4])
            sentences = []
            image['filepath'] = d
            image['filename'] = dataset_file
            image['split'] = d[:-4]
            #檔名長度
            #image['cocoid'] = int(dataset_file[-14:-4])
            image['cocoid'] = img_id
            image['imgid'] = img_id
            #filepath = d
            #filename = dataset_file
            #split = d[:-4]
            #coco_id = int(dataset_file[-14:-4])


            for i in range(sentence_num):
                #自己輸入
                raw = input("Enter sentences: ")
                #檔案輸入
                #raw = fp_sentence[sentence_id]
                sentence_id += 1
                tokens = raw.replace('.','').replace(',','').split(' ')
                sentids.append(sent_id)
                sentence['tokens'] = tokens
                sentence['raw'] = raw
                sentence['imgid'] = img_id
                sentence['sentid'] = sent_id
                #j_sentences['tokens'] = tokens
                #j_sentences['raw'] = raw 
                #j_sentences['imgid'] = img_id
                #j_sentences['sentid'] = sent_id
                sentences.append(sentence)
                sentence = {"tokens":"" ,"raw": "","imgid": 0, "sentid": 0}
                sent_id += 1
            
            image['sentences'] = sentences
            image['sentids'] = sentids
            print(image)
            sentids = []
            sentences = []
            info.append(image)
            my_json = {"images": [], "dataset":"coco"}
            #image in json["images"]
            image = {"filepath": "","sentids": [], "filename": "","imgid": 0,"split": "","sentences":[], "cocoid":0}
            #sentence in image["sentences"]
            sentence = {"tokens":"" ,"raw": "","imgid": 0, "sentid": 0}
            print(info)

            #info = {"filepath": filepath, "sentids": sentids, "filename": filename, "imgid": img_id, "split": split,  "sentences": sentences}
            #images_json.append(str(info) + ',\"cocoid\":' + str(coco_id) )

            img_id += 1

my_json["images"] = info
print('====================')
print(str(my_json))
print('********************')

with open(json_path,"w") as file:
    json=json.dump(my_json, file)


