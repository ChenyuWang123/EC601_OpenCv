import numpy as np
import cv2
#cv2.namedWindow('orignal_image', cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
#cv2.imshow('orignal_image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

names=('Lenna.png','coins.png','baboon.jpg','cameraman.png','rice_grains.jpg','barbara.png')
for i in names:
    src='C:/Users/Chenyu/Desktop/EC601/OpenCv/'
    src_new=src+i
    img=cv2.imread(src_new,cv2.IMREAD_COLOR)
    px_RGB=img[20,25]
    print(i+' '+'RGB'+' ',px_RGB)
    Red,Green,Blue=cv2.split(img)
    cv2.imwrite(src+'Red_'+i,Red)
    cv2.imwrite(src+'Green_'+i,Green)
    cv2.imwrite(src+'Blue_'+i,Blue)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    H,S,V=cv2.split(hsv)
    px_HSV=hsv[20,25]
    print(i+' '+'HSV'+' ',px_HSV)
    cv2.imwrite(src+'H_'+i,H)
    cv2.imwrite(src+'S_'+i,S)
    cv2.imwrite(src+'V_'+i,V)
    ycrcb=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
    Y,CR,CB=cv2.split(ycrcb)
    px_YCRCB=ycrcb[20,25]
    print(i+' '+'YCRCB'+' ',px_YCRCB)
    cv2.imwrite(src+'Y_'+i,Y)
    cv2.imwrite(src+'CR_'+i,CR)
    cv2.imwrite(src+'CB_'+i,CB)
