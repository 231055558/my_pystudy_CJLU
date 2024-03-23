import cv2
import json
f = open("222.json", 'r')
load_dict = json.load(f)
box = load_dict['shapes'][1]['points']
image = cv2.imread('222.jpg') # 打开第1张图
image2 = cv2.imread('001.jpg') #打开第2张图
image[int(box[0][0]):int(box[0][1])+22,int(box[1][0]):int(box[1][1]), :] = image2  #切片，把左上角变为第2张图的内容。这里一定要保证image比image2的分辨率要大，否则就会数组访问越界。
cv2.imshow('show', image) # 显示结果
cv2.waitKey(0) #暂停，按任意键继续