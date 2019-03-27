import os
import json


class CloudFile(object):
    def __init__(self, clouldfile=".cloudfile"):
        self._cloudfile = ".cloudfile"
        if os.path.isfile(self._cloudfile):
            self.dct = json.load(open(clouldfile, "r"))
        else:
            self.dct = {}
            self.save_json()

    def save_json(self):
        json.dump(self.dct, open(self._cloudfile, "w"))

    def save_file(self, file):
        assert os.path.isfile(file)
        path = os.path.normpath(file)
        file = path.split(os.sep)[-1]
        path = os.path.join(*path.split(os.sep)[:-1])
        self.dct[path] = file
        self.save_json()
