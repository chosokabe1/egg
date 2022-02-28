import cv2
import glob

def a_image_max_height_width(img_path):
    im = cv2.imread(img_path)
    h, w, c = im.shape
    if h >= w:
        max = h
    else:
        max = w
    
    return max

def dir_max(dir_path):
    img_paths = glob.glob(dir_path + "/*")
    max = 0
    for img_path in img_paths:
        tmp = a_image_max_height_width(img_path)
        if max < tmp:
            max = tmp
        
    return max

def dirs_max(dir_paths):
    max = 0
    for dir_path in dir_paths:
        tmp = dir_max(dir_path)

        if max < tmp:
            max = tmp
        
    return max

dir_list = ['../../particular-cut/3-1/egg/2', \
            '../../particular-cut/3-1/egg/3', \
            '../../particular-cut/3-1/egg/5', \
            '../../particular-cut/3-1/egg/7', \
            '../../particular-cut/3-1/no-egg/1', \
            '../../particular-cut/3-1/no-egg/10', \
            '../../particular-cut/3-1/no-egg/11']
print(dirs_max(dir_list))
