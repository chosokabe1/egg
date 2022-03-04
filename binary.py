import cv2
from PIL import Image
import numpy as np
IMG_SIZE = 32

def a_image_max_height_width(im):
    h, w= im.shape
    if h >= w:
        max = h
    else:
        max = w
    
    return max

def make_square(im,MAX_HW):
    h, w= im.shape

    out_im = np.zeros((MAX_HW,MAX_HW))
    print(im)
    out_im[0:h, 0:w] = im
    
    cv2.imwrite("./a.jpg", out_im)

    return out_im

img = cv2.imread('../0.jpg',0)
img = cv2.bitwise_not(img)
max_hw = a_image_max_height_width(img)
# square = make_square(img,max_hw)
# square = cv2.resize(square, dsize=(IMG_SIZE,IMG_SIZE))
# cv2.imwrite("./b.jpg", square)
# img_sobel = cv2.Sobel(square, cv2.CV_8U, 1, 0, ksize=3)
# cv2.imwrite("./c.jpg", img_sobel)
imgCopy = np.uint8(img)
img_canny = cv2.Canny(imgCopy, 40, 40)

cv2.imwrite("./d.jpg", img_canny)
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img_canny, cv2.MORPH_CLOSE, kernel)
closing_opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
cv2.imwrite("./g.jpg", closing_opening)

kernel1 = np.ones((35,35),np.uint8)
kernel2 = np.ones((135,135),np.uint8)

closing1 = cv2.morphologyEx(img_canny, cv2.MORPH_CLOSE, kernel1)
closing1_opening1 = cv2.morphologyEx(closing1, cv2.MORPH_OPEN, kernel1)

closing1_opening2 = cv2.morphologyEx(closing1, cv2.MORPH_OPEN, kernel2)

closing1_opening1_closing2 = cv2.morphologyEx(closing1_opening1, cv2.MORPH_CLOSE, kernel2)
cv2.imwrite("./g.jpg", closing1_opening1_closing2)


closing3 = cv2.morphologyEx(img_canny, cv2.MORPH_CLOSE, kernel2)
cv2.imwrite("./e.jpg", closing1_opening1)
cv2.imwrite("./f.jpg", closing3)

square = make_square(closing1_opening1_closing2,max_hw)
square = cv2.resize(square, dsize=(IMG_SIZE,IMG_SIZE))
cv2.imwrite("./d.jpg", square)

npsquare = np.array(Image.open('./d.jpg'))
print(npsquare)





