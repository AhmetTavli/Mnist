from numpy import arange
from os.path import join
from os import getcwd, mkdir


class Directory:
    DIR_MNIST = join(getcwd(), "mnist")
    DIR_TRAIN = join(DIR_MNIST, "train")
    DIR_TEST = join(DIR_MNIST, "test")

    def __init__(self):
        self.dirs = [self.DIR_MNIST, self.DIR_TRAIN, self.DIR_TEST]
        self.train_test_dir = [self.DIR_TRAIN, self.DIR_TEST]
        self.create_dirs()
        self.create_labels()

    def create_dirs(self):
        for i in self.dirs:
            mkdir(i)

    def create_labels(self):
        for i in self.train_test_dir:
            for j in arange(10):
                label_dir = join(str(i), str(j))
                mkdir(label_dir)
