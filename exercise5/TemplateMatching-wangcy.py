import numpy as np
import cv2

def TemplateMatching(src, temp, stepsize):
    mean_t = np.mean(temp)
    var_t = np.var(temp)
    temp_w = temp.shape[0]
    temp_l = temp.shape[1]
    max_corr = 0
    sumi = 0

    for i in range(0, src.shape[0] - temp.shape[0], stepsize):
        for j in range(0, src.shape[1] - temp.shape[1], stepsize):
            scan = src[i:(i+temp_w),j:(j+temp_l)]
            mean_s = np.mean(scan)
            var_s = np.var(scan)
            sumi = 0
            for k in range(0,temp_w):
                for l in range(0,temp_l):
                    sumi=sumi+(scan[k][l]-mean_s)*(temp[k][l]-mean_t)
                   # print(sumi)
            corr = sumi/(temp_w*temp_l*var_s*var_t)
            print(corr)

            if corr > max_corr:
                max_corr = corr
                x = j
                y = i

    return x,y
x=0
y=0
temp_w=0
temp_l=0
source_img = cv2.imread('C:/Users/Chenyu/Desktop/source_img.jpg',0) # read image in grayscale
temp = cv2.imread('C:/Users/Chenyu/Desktop/template_img.jpg',0) # read image in grayscale
x,y = TemplateMatching(source_img, temp, 10)
##x=location[0];
##y=location[1];
print(x,y)
match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)
print(temp.shape)

cv2.line(match_img,(x,y),(x+241,y),(0,0,255),thickness=4)
cv2.line(match_img,(x,y),(x,y+138),(0,0,255),thickness=4)
cv2.line(match_img,(x,y+138),(x+241,y+138),(0,0,255),thickness=4)
cv2.line(match_img,(x+241,y),(x+241,y+138),(0,0,255),thickness=4)

# Display the template image and the matching result
cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
cv2.imwrite('TemplateImage.jpg', temp)
cv2.imwrite('MyTemplateMatching.jpg', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
