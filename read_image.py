import cv2
import os
import sys


#path = input("Enter want read image file root path:")
path = '/media/cvlab/5CA28BFDA28BDA42/coco_dataset/val2014'

#count file num
for dirPath, dirNames, fileNames in os.walk(path):
    for image_file in fileNames:
        print(image_file)
        img = cv2.imread(os.path.join(path, image_file))
        cv2.imshow('image' ,img)

        key = cv2.waitKey(0)
        if key == 27 or key == ord('q'):
            cv2.destroyAllWindows()
            sys.exit("stop program") 

cv2.destroyAllWindows()