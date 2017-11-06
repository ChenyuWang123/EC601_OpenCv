import cv2
import numpy as np
    
location='C:/Users/Chenyu/Desktop/EC601/OpenCv/exercise4/'
img = cv2.imread(location+'Lenna.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite(location+'Lenna.png',gray)
    
ret,dst=cv2.threshold(gray,127, 255, 2 );
cv2.imwrite(location+'Lenna_threshold.png',dst)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imwrite(location+'Lenna_binary.png',thresh1)
    
threshold1 = 27
threshold2 = 125
ret,binary_image1 = cv2.threshold(gray,threshold1,255,cv2.THRESH_BINARY)
ret,binary_image2 = cv2.threshold(gray,threshold2,255,cv2.THRESH_BINARY_INV)
band_thresholded_image=np.bitwise_and(binary_image1, binary_image2);
cv2.imwrite(location+'Lenna_band.png',band_thresholded_image)
    
ret,semi_thresholded_image=cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
semi_thresholded_image=np.bitwise_and( gray, semi_thresholded_image )
cv2.imwrite(location+'Lenna_semi.png',semi_thresholded_image)
   
adaptive_thresh=cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10 )
cv2.imwrite(location+'Lenna_adptive.png',adaptive_thresh)
