import os

from tests.utils import ini_files, del_folder

import cloudfile


def test_make_cloudfile():
    ini_files({"foo": ["bar.txt", {"foo2": "bar2.txt"}]})
    cloudfile.save("foo")

    assert os.path.isfile(".cloudfile")
    os.remove(".cloudfile")
    del_folder("foo")
