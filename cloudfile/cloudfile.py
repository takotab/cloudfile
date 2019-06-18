import os
import json


class CloudFile(object):
    def __init__(self, clouldfile="cloudfile.json", unit_test_link_dct=None):
        self._cloudfile = clouldfile
        self.service = None
        if os.path.isfile(self._cloudfile):
            self.dct = json.load(open(clouldfile, "r"))
        else:
            self.dct = {} if unit_test_link_dct is None else unit_test_link_dct
            self.save_json()

    def get_service(self):
        from .google import get_service

        if self.service is None:
            self.service = get_service()
        return self.service

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

    def __setitem__(self, key, item):
        self.dct[key] = item

    def upload_file(self, file, hard=False):
        if file in self.dct and not hard:
            print(
                f"Did not upload {file}. File already exist.\nRun `cloudfile add_file {dir} --hard=True` to download this file anyway."
            )
            return None, None
        from .google import upload_file

        link, file_id = upload_file(self.get_service(), file)
        self.dct[file] = link
        self.save_json()
        return link, file_id

    def keys(self):
        return list(self.dct.keys())
