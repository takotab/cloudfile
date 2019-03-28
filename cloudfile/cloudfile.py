import os
import json


class CloudFile(object):
    def __init__(self, clouldfile="cloudfile.json", unit_test_link_dct=None):
        self._cloudfile = clouldfile
        if os.path.isfile(self._cloudfile):
            self.dct = json.load(open(clouldfile, "r"))
        else:
            self.dct = {} if unit_test_link_dct is None else unit_test_link_dct
            self.save_json()

    def save_json(self):
        json.dump(self.dct, open(self._cloudfile, "w"))

    def save_file(self, file):
        assert os.path.isfile(file)
        self.dct[file] = None
        self.save_json()

    def items(self) -> [(str, str)]:
        return self.dct.items()

    def __getitem__(self, item):
        return self.dct[item]
