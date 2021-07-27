import json

filename = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/annotations/dataset_coco.json'
#find = input('find:')

with open(filename) as file: # 以讀取模式開啟檔案(若沒有第二個參數都是預設成讀取模式)
    numbers=json.load(file)

strjson = str(numbers)

while True:
    find = input('fild: ')
    same = 0
    count = 0
    print_switch = False

    for i in range(len(strjson)):
        if not print_switch:
            if strjson[i] == find[0]:
                for j, num in zip(range(len(find)),range(i,i+len(find))):
                    
                    if strjson[num] == find[j]:
                        same += 1
                    else:
                        same = 0
                        break
                    if same == len(find):
                        print_switch = True
        if print_switch:
            print(strjson[i],end = '')
            count += 1
            if count > 2000:
                break

            
        