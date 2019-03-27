import json
import os

from tests.utils import ini_files, del_folder

import cloudfile

cloudfile_dct = {
    "foo/bar.txt": "https://docs.google.com/document/d/1yfcBYMKzaBsUsLmuoitqT8spXGVKiiGo9MxJ8eBjNgM/export?format=txt",
    "foo/foo2/bar2.txt": "https://docs.google.com/document/d/1KQNXOMEqzEl9D5IAyzecj_CiCphobEdaou9oNhzOZgg/export?format=txt",
}


def test_restore():
    if os.path.isfile(".clouldfile"):
        os.remove(".cloudfile")
    del_folder("foo")

    json.dump(cloudfile_dct, open(".cloudfile", "w"))
    cloudfile.restore()
    assert os.path.isdir("foo")
    assert os.path.isdir("foo/foo2")
    assert os.path.isfile("foo/bar.txt")
    assert os.path.isfile("foo/foo2/bar2.txt")
    os.remove(".cloudfile")
