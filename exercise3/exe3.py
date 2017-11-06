import cv2
import numpy as np

def Add_gaussian_Noise(pic, mean, sigma):
    
    noice_pic=pic.copy()
    cv2.randn(noice_pic,mean,sigma)
    cv2.add(pic, noice_pic, noice_pic)
    
    return noice_pic

def Add_salt_pepper_Noise(pic, pa, pb):
    num1 = int(pic.shape[0]*pic.shape[1]*pa)
    num2 = int(pic.shape[0]*pic.shape[1]*pb)
    noisepic=pic
    
    for i in range(num1):
        a=np.random.randint(0,pic.shape[0]-1)
        b=np.random.randint(0,pic.shape[1]-1)
        noisepic[a,b]=0
        
    for i in range(num2):
        c=np.random.randint(0,pic.shape[0]-1)
        d=np.random.randint(0,pic.shape[1]-1)
        noisepic[c,d]=255
        
    return noisepic

def main():
    mean = 20
    sigma = 100
    pa = 0.03
    pb = 0.03
    pic = cv2.imread("C:/Users/Chenyu/Desktop/EC601/OpenCv/exercise 2/Lenna.png")
    gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("./LennaGray.png",gray)
    
    g_n_Image = Add_gaussian_Noise(gray,mean,sigma)
    cv2.imwrite("./gaussian_noise.png",g_n_Image)    
    p_s_Image=Add_salt_pepper_Noise(gray,pa,pb)
    cv2.imwrite("./pepper_salt_noise.png",p_s_Image)
    
    boxfilter_img = cv2.boxFilter(g_n_Image, -1, (3, 3))
    cv2.imwrite("./gaussian_Boxfilter.png",boxfilter_img)
    gaussfilter_img=cv2.GaussianBlur(g_n_Image, (3,3), 1.5, 3)
    cv2.imwrite("./gaussian_Gaussfilter.png",gaussfilter_img)
    medianfilter_img=cv2.medianBlur(g_n_Image,5)
    cv2.imwrite("./gaussian_Medianfilter.png",medianfilter_img)
    boxfilter_img = cv2.boxFilter(p_s_Image, -1, (3, 3))
    cv2.imwrite("./pepper_salt_Boxfilter.png",boxfilter_img)
    gaussfilter_img=cv2.GaussianBlur(p_s_Image, (3,3), 1.5, 3)
    cv2.imwrite("./pepper_salt_Gaussfilter.png",gaussfilter_img)
    medianfilter_img=cv2.medianBlur(p_s_Image,5)
    cv2.imwrite("./pepper_salt_Medianfilter.png",medianfilter_img)
    
if __name__ == "__main__":
    main()
