import json
import os

from tests.utils import ini_files, del_folder

import cloudfile

cloudfile_dct = {
    "foo/bar.txt": "https://docs.google.com/document/d/1yfcBYMKzaBsUsLmuoitqT8spXGVKiiGo9MxJ8eBjNgM/export?format=txt",
    "foo/foo2/bar2.txt": "https://docs.google.com/document/d/1KQNXOMEqzEl9D5IAyzecj_CiCphobEdaou9oNhzOZgg/export?format=txt",
    "foo/foo1/foo_dir/bar.csv": "https://google.com",
}


def create_dct():
    json.dump(cloudfile_dct, open("cloudfile.json", "w"))


def test_restore():
    if os.path.isfile("clouldfile.json"):
        os.remove("cloudfile.json")
    del_folder("foo")

    create_dct()
    cloudfile.restore()
    assert os.path.isdir("foo")
    assert os.path.isdir("foo/foo2")
    assert os.path.isfile("foo/bar.txt")
    assert os.path.isfile("foo/foo2/bar2.txt")
    os.remove("cloudfile.json")


def test_restore_file():
    if os.path.isfile("clouldfile.json"):
        os.remove("cloudfile.json")
    del_folder("foo")

    create_dct()
    cloudfile.restore_file("foo/bar.txt")
    assert os.path.isdir("foo")
    assert os.path.isfile("foo/bar.txt")
    os.remove("cloudfile.json")
