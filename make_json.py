import json
import os
import cv2

root = "/home/cvlab/ContourNet/datasets/ic15/my_data/train/"


#資料夾內所有圖片
all_file = 0
for dirPath, dirNames, fileNames in os.walk(root):
    for f in fileNames:
        #print (f)
        all_file += 1



#放入圖片名稱 圖片大小 編號
images = []
# widt, height , file name, id = file name
for i in range(all_file):
    fileid = i
    filename = str(i).zfill(7) + ".jpg"
    img = cv2.imread(root + filename)
    width = img.shape[1]
    height = img.shape[0]

    info = {"width": width, "date_captured": "", "license": 0, "flickr_url": "", "file_name": filename, "id": fileid, "coco_url": "", "height": height}
    images.append(info)
data['images'] = images


file = '/home/cvlab/ContourNet/datasets/ic15/my_data/my_data.json'
with open(file, 'r') as obj:
    my_data = json.load(obj)

count = 0
annotations = []
for img in my_data:
    img_id = int(img['image'][:-4])
    for my_annotations in img['annotations']:
        segmentation = []
        bbox = []
        keypoints = []
        x = int(my_annotations['coordinates']['x'])
        y = int(my_annotations['coordinates']['y'])
        dx = int(my_annotations['coordinates']['width'])
        dy = int(my_annotations['coordinates']['height'])
        dx_cut = int(dx / 4)
        dy_cut = int(dy / 4)

        x1 = x - int(dx / 2)
        y1 = y - int(dy / 2)
        segmentation.append([x1, y1, x1+dx, y1, x1+dx, y1+dy, x1, y1+dy])
        bbox = [x1, y1, dx, dy]
        area = dx * dy
        keypoints = [x1+2*dx_cut, y1+2*dy_cut, 2, x1+dx_cut, y1+2*dy_cut, 2, x1+dx_cut, y1+2*dy_cut, 2, x1+3*dx_cut, y1+2*dy_cut, 2, x1+3*dx_cut, y1+2*dy_cut, 2, x1+2*dx_cut, y1+dy_cut, 2, x1+2*dx_cut, y1+2*dy_cut, 2, x1+2*dx_cut, y1+2*dy_cut, 2, x1+2*dx_cut, y1+3*dy_cut, 2, x1+3*dx_cut, y1+2*dy_cut, 2]
        info = {"image_id": img_id, "segmentation": segmentation,  "bbox": bbox, "area": area, "category_id": 1, "iscrowd": 0, "id": count, "keypoints": keypoints}
        count += 1
        annotations.append(info)
data['annotations'] = annotations

save_root = '/home/cvlab/ContourNet/datasets/ic15/annotations/my_data_final.json'
with open(file, 'w') as obj:
    json.dump(data, obj)
