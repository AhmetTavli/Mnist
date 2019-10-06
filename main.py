from images import SaveImages
from directory import Directory
from tensorflow.keras.datasets import mnist

if __name__ == "__main__":
    dir_object = Directory()
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    SaveImages(data=x_train, label=y_train, path=dir_object.DIR_TRAIN)
    SaveImages(data=x_test, label=y_test, path=dir_object.DIR_TEST)
