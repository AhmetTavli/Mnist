from os.path import join
from matplotlib.pyplot import cm, imsave


class SaveImages:
    def __init__(self, data, label, path):
        self.data = data
        self.label = label
        self.path = path
        self._save()

    def _save(self):
        for i, x in enumerate(self.data):
            iname = "{}_{}.png".format(str(self.label[i]), str(i))
            fname = join(self.path, str(self.label[i]), iname)
            imsave(fname=fname, arr=self.data[i], cmap=cm.binary)
