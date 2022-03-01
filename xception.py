from keras.applications.xception import Xception
from keras.datasets.cifar10 import load_data
from keras.layers import Input
#from keras.utils import to_categorical
#変更
from tensorflow.keras.utils import to_categorical
from PIL import Image #変更
from keras.preprocessing.image import array_to_img, img_to_array, load_img#変更
import glob
import numpy as np
import csv
import requests # line
# IMAGE_SIZE = 1644
IMAGE_SIZE = 384
CSV_NAME = "384history.csv"
BY = 3

#ラインに通知する
def line_notify(message):
    line_notify_token = 'Fr43LJvmOI9rX2le4mVYALcdFJoxIifLJ418fvMidq2'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token} 
    requests.post(line_notify_api, data=payload, headers=headers)

# ディレクトりの全画像をdatasetに加え，ラベルをつける
def load_from_dir(dir_path, dataset, labelset):
    img_paths = sorted(glob.glob(dir_path + "/*"))
    counter = 0
    for img_path in img_paths:
        if counter == 1:
            img = Image.open(img_path)
            img = img.convert("RGB")
            img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
            data = np.array(img)
            dataset.append(data)
            # 画像pathに'no'が含まれていれば'no-egg'なのでラベル0をつける
            if 'no' in img_path:
                labelset.append(0)
            else:
                labelset.append(1)

            counter = 0

        counter += 1
    return dataset, labelset


def load():
    train_paths = ["../square/3-1/egg/3",\
                  "../square/3-1/egg/5",\
                  "../square/3-1/no-egg/1"]
    test_paths = ["../square/3-1/egg/2",\
                 "../square/3-1/no-egg/10"]

    x_train = []
    y_train = []
    x_test = []
    y_test = []
    for train_path in train_paths:
        x_train, y_train= load_from_dir(train_path, x_train, y_train)

    for test_path in test_paths:
        x_test, y_test = load_from_dir(test_path, x_test, y_test)

    x_train = np.array(x_train, dtype=np.uint8)
    y_train = np.array(y_train, dtype=np.uint8)
    x_test = np.array(x_test, dtype=np.uint8)
    y_test = np.array(y_test, dtype=np.uint8)


    return x_train, y_train, x_test, y_test

def train():
    x_train, y_train, x_test, y_test = load()
    print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
    print("あ")
    x_train = x_train.astype(np.float32)
    x_train = x_train / 255.
    x_test = x_test.astype(np.float32)
    x_test = x_test / 255.
    print("あ")

    n_labels = len(np.unique(y_train))
    y_train = to_categorical(y_train, n_labels)
    y_test = to_categorical(y_test, n_labels)
    print(y_train.shape, y_test.shape)
    print("あ")

    input = Input(shape=(IMAGE_SIZE, IMAGE_SIZE, 3))
    model = Xception(weights=None, input_tensor=input, classes=n_labels)
    model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])
    h = model.fit(x_train, y_train, epochs=500, validation_data=(x_test, y_test))

    for key in h.history.keys():
        print(key)

    loss = h.history["loss"]
    val_loss = h.history["val_loss"]
    accuracy = h.history["accuracy"]
    val_accuracy = h.history["val_accuracy"]
    with open(CSV_NAME, "wt", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["EPOCH", "ACC(TRAIN)", "ACC(TEST)", "LOSS(TRAIN)", "LOSS(TEST)"])
        for i in range(len(loss)):
            writer.writerow([i+1, accuracy[i], val_accuracy[i], loss[i], val_loss[i]])

    return model


if __name__ == "__main__":
    import sys, keras, tensorflow
    print("Python %s" % sys.version)
    print("Keras %s" % keras.__version__)
    print("TensorFlow %s" % tensorflow.__version__)

    model = train()
    model.save("cifer10+xception.hdf5")

    message = "終了しました"
    line_notify(message)