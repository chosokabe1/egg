import cv2
import glob
import os
import sys

def txt_number_of_lines(path):
    with open(path) as f:
        s = f.readlines()
        return len(s)

def kiri(yolo_split,jpg_path,count,out_path):
    img = cv2.imread(jpg_path)

    if yolo_split:
        center_x_float = float(yolo_split[1])
        center_y_float = float(yolo_split[2])
        width_float    = float(yolo_split[3])
        height_float   = float(yolo_split[4])
        print("count = " + str(count))
        print(yolo_split[0])
        print(center_x_float)  
        print(center_y_float)
        print(width_float)  
        print(height_float)
        print(img.shape)
        center_x_int = round(img.shape[1] * center_x_float)
        center_y_int = round(img.shape[0] * center_y_float)
        width_int    = round(img.shape[1] * width_float)
        height_int   = round(img.shape[0] * height_float)
        kiri_left = center_x_int - width_int // 2
        kiri_right = kiri_left + width_int
        kiri_top = center_y_int - height_int // 2
        kiri_bottom = kiri_top + height_int
        kiri_img = img[kiri_top:kiri_bottom, kiri_left:kiri_right]
        cv2.imwrite(out_path + '/' + str(count) + '.jpg', kiri_img)

def make_path(path):
    # ディレクトリが存在しない場合、ディレクトリを作成する
    if not os.path.exists(path):
        os.makedirs(path)

#特定の線虫idの線虫を切り出す
def particular_elegans_cut(elegans_id, out_path):
    count = 0

    for txt_path in txt_paths:
        if 'classes' in txt_path:
            continue
    
        jpg_path = os.path.splitext(txt_path)[0] + '.jpg'
        with open(txt_path) as f:
            s = f.readlines()
            for line in s:
                split = line.split()
                if not split[0] == str(elegans_id):
                    continue
                kiri(split,jpg_path,count,out_path)
                count += 1 

def a():
    for elegans_id in range(classes_number):
        print('elegans_id =' +  str(elegans_id))
        out_path = '../../particular-cut/' + str(elegans_id)
        make_path(out_path)
        particular_elegans_cut(elegans_id, out_path)

args = sys.argv
in_path = args[1]
txt_paths = sorted(glob.glob(in_path + "/*.txt"))
classes_number = txt_number_of_lines(in_path + "/classes.txt")
a()