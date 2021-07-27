import numpy as np
import cv2 as cv
import json

file = '/home/cvlab/ContourNet/datasets/ic15/annotations/ic15_test.json'
with open(file, 'r') as obj:
    data_org = json.load(obj)

#print(data_org["annotations"])
#input()
#data = {"image_id": 30, "segmentation": [[104, 0, 182, 1, 160, 82, 124, 75]], "match_type": 3, "bbox": [104, 0, 79, 83], "area": 6557, "category_id": 1, "iscrowd": 0, "id": 380, "keypoints": [142.5, 39.5, 2, 123.25, 39.5, 2, 133.25, 39.5, 2, 151.25, 39.5, 2, 162.25, 39.5, 2, 142.5, 19.75, 2, 142.5, 20.25, 2, 142.5, 57.25, 2, 142.5, 60.75, 2, 140, 53, 2]}
data_list = data_org["annotations"]

output_root = '/home/cvlab/ContourNet/datasets/ic15/json_to_image/'
num = 0

for data in data_list:

    if data['image_id'] < 10:
        img = cv.imread('/home/cvlab/ContourNet/datasets/ic15/ic15_test_images/000000'+ str(data['image_id']) +'.jpg')
    elif data['image_id'] < 100:
        img = cv.imread('/home/cvlab/ContourNet/datasets/ic15/ic15_test_images/00000'+ str(data['image_id']) +'.jpg')
    else:
        img = cv.imread('/home/cvlab/ContourNet/datasets/ic15/ic15_test_images/0000'+ str(data['image_id']) +'.jpg')


    point_size = 1
    point_color = (0, 0, 255) # BGR
    thickness = 4 # 可以为 0 、4、8

    # 要画的点的坐标
    keypoints_list = data["keypoints"]
    segmentation_list = data["segmentation"][0]
    bbox_list = data["bbox"]

    keypoints_point_list = []
    segmentation_point_list = []
    bbox_point_list = []

    keypoints = []
    segmentation = []
    bbox = []

    for point in keypoints_list:
        keypoints_point_list.append(int(point))
    for point in segmentation_list:
        segmentation_point_list.append(int(point))
    for point in bbox_list:
        bbox_point_list.append(int(point))


    for point in range(0,len(segmentation_point_list),2):
        segmentation.append([segmentation_point_list[point],segmentation_point_list[point+1]])

    bbox.append([bbox_point_list[0],bbox_point_list[1]])
    bbox.append([bbox_point_list[0]+bbox_point_list[2],bbox_point_list[1]+bbox_point_list[3]])
    squer_x = int(bbox_point_list[2] / 4)
    squer_y = int(bbox_point_list[3] / 4)
    '''
    squer_list = [
        [bbox_point_list[0]+squer_x, bbox_point_list[1]+squer_y],[bbox_point_list[0]+squer_x*2, bbox_point_list[1]+squer_y],[bbox_point_list[0]+squer_x*3, bbox_point_list[1]+squer_y],
        [bbox_point_list[0]+squer_x, bbox_point_list[1]+squer_y*2],[bbox_point_list[0]+squer_x*2, bbox_point_list[1]+squer_y*2],[bbox_point_list[0]+squer_x*3, bbox_point_list[1]+squer_y*2],
        [bbox_point_list[0]+squer_x, bbox_point_list[1]+squer_y*3],[bbox_point_list[0]+squer_x*2, bbox_point_list[1]+squer_y*3],[bbox_point_list[0]+squer_x*3, bbox_point_list[1]+squer_y*3]]
    '''
    squer_list = [
                                                                    [bbox_point_list[0]+squer_x*2, bbox_point_list[1]+squer_y],
        [bbox_point_list[0]+squer_x, bbox_point_list[1]+squer_y*2],[bbox_point_list[0]+squer_x*2, bbox_point_list[1]+squer_y*2],[bbox_point_list[0]+squer_x*3, bbox_point_list[1]+squer_y*2],
                                                                    [bbox_point_list[0]+squer_x*2, bbox_point_list[1]+squer_y*3]]


    keypoints.append([keypoints_point_list[0],keypoints_point_list[1]])
    for point in range(3,len(keypoints_point_list),3):
        keypoints.append([keypoints_point_list[point],keypoints_point_list[point+1]])

    i = 0
    color = [(255,250,0),(0,206,209),(0,191,255),(238,230,133),(238,99,99),(255,130,71),(208,32,144),(224,102,255),(176,48,96),(0,255,0)]
    for point in keypoints:
        point = tuple(point)
        cv.circle(img, point, point_size, point_color, thickness)
        cv.putText(img, str(i), point, cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color[i], 1, cv.LINE_AA)
        i += 1

    point_color = (0, 255, 0) # BGR
    
    for point in segmentation:
        point = tuple(point)
        cv.circle(img, point, point_size, point_color, thickness)
        #cv.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
        

    cv.line(img, tuple(segmentation[0]), tuple(segmentation[1]), (0, 255, 0), 2)
    cv.line(img, tuple(segmentation[1]), tuple(segmentation[2]), (0, 255, 0), 2)
    cv.line(img, tuple(segmentation[2]), tuple(segmentation[3]), (0, 255, 0), 2)
    cv.line(img, tuple(segmentation[3]), tuple(segmentation[0]), (0, 255, 0), 2)

    point_color = (255,0,0)
    for point in bbox:
        point = tuple(point)
        cv.circle(img, point, point_size, point_color, thickness)

    point_color = (255,255,0)
    for point in squer_list:
        point = tuple(point)
        cv.circle(img, point, point_size, point_color, thickness)



    cv.namedWindow("image")
    cv.imshow('image', img)
    output_path = output_root + 'type' + str(data["match_type"]) + '_id' + str(data["image_id"]) + '_' + str(num) + '.jpg'
    cv.imwrite(output_path, img)
    num += 1
    #cv.waitKey (0)
    key = cv.waitKey(1)
    if key == ord('q') or key == 27: # Esc
        break

cv.destroyAllWindows()
