import numpy as np
import cv2 as cv
import os
'''
img_list = []
point_list = []
fp = open('/home/cvlab/ContourNet/datasets/ic15/google_result/0000001.txt','r')
for line in fp:
    point_list.append(line.replace('\n',''))
#print(point_list)
for i in point_list:
    print(i.split('),(')[0][1:])
input('==========')
'''
img_list = []
point_list = []
for dirPath, dirNames, fileNames in os.walk("/home/cvlab/下載/google/"):
    for f in fileNames:
        img_list.append(f)
img_list.sort()
txt_list = []
for dirPath, dirNames, fileNames in os.walk("/home/cvlab/下載/google_txt/"):
    for f in fileNames:
        txt_list.append(f)
txt_list.sort()


for img_name, txt_name in zip(img_list, txt_list):
    img = cv.imread('/home/cvlab/下載/google/' + img_name)
    txt = open('/home/cvlab/下載/google_txt/' + txt_name,'r')
    first = True
    for line in txt:
        if first:
            first = False
        else:
            point_list = []
            point_list.append(line.replace('\n',''))

            point = []
            for i in point_list:
                points = i.replace('(','').replace(')','').split(',')

                point.append(int(points[0]))
                point.append(int(points[1]))
                point.append(int(points[4]))
                point.append(int(points[5]))
                #print(point)
                #input('========')
                img = cv.rectangle(img, (point[0],point[1]), (point[2],point[3]), (0,255,0), 2)

    cv.imwrite('/home/cvlab/下載/google_img_result/' + img_name, img)
    cv.namedWindow("image")
    cv.imshow('image', img)
    cv.waitKey(0)
#for point in points_list:
#	cv.circle(img, point, point_size, point_color, thickness)


cv.destroyAllWindows()
