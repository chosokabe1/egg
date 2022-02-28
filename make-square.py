import cv2
import glob
import numpy as np
import os
MAX_HW = 1644


def make_path(path):
    # ディレクトリが存在しない場合、ディレクトリを作成する
    if not os.path.exists(path):
        os.makedirs(path)

def make_square(img_path):
    im = cv2.imread(img_path)
    h, w, c = im.shape

    out_im = np.zeros((MAX_HW,MAX_HW,3))

    out_im[0:h, 0:w] = im
    out_path = img_path.replace('particular-cut', 'square')   
    cv2.imwrite(out_path, out_im)

def a(dir_path):
    img_paths = glob.glob(dir_path + "/*")
    out_path = dir_path.replace('particular-cut', 'square')
    make_path(out_path)  
    for img_path in img_paths:
        make_square(img_path)


# dir_list = ['../../particular-cut/3-1/egg/2', \
#             '../../particular-cut/3-1/egg/3', \
#             '../../particular-cut/3-1/egg/5', \
#             '../../particular-cut/3-1/egg/7', \
#             '../../particular-cut/3-1/no-egg/1', \
#             '../../particular-cut/3-1/no-egg/10', \
#             '../../particular-cut/3-1/no-egg/11']

dir_list = ['../../particular-cut/3-1/egg/2']


for dir in dir_list:
    a(dir)

