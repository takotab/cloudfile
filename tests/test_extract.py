import json
import os

import cloudfile
from cloudfile.extract import extract
from tests.utils import del_folder


def test_extract():

    filename = "test.txt"
    zipfilename = "zipper_test.7z"
    with open(filename, "w") as f:
        f.write("hello world")
    os.system("7z a " + zipfilename + " " + filename)
    os.remove(filename)

    extract(zipfilename)
    assert os.path.isfile(filename)
    os.remove(filename)
    os.remove(zipfilename)


def test_extract_folder():
    cloudfile_dct = {
        "foo.7z": "https://drive.google.com/uc?export=download&id=1iU8DK-ZMzHz3fANAcrcYwNW4K71cTjeJ"
    }
    json.dump(cloudfile_dct, open("cloudfile.json", "w"))

    cloudfile.restore()
    assert os.path.isdir("foo")
    assert os.path.isdir("foo/foo2")
    assert os.path.isfile("foo/bar.txt")
    assert os.path.isfile("foo/foo2/bar2.txt")
    os.remove("cloudfile.json")
    os.remove("foo.7z")
    del_folder("foo")


def test_extract_subfolder():
    cloudfile_dct = {
        "fubar/foo.7z": "https://drive.google.com/uc?export=download&id=1iU8DK-ZMzHz3fANAcrcYwNW4K71cTjeJ"
    }
    json.dump(cloudfile_dct, open("cloudfile.json", "w"))

    cloudfile.restore()
    assert os.path.isdir("fubar")
    assert os.path.isdir("fubar/foo/foo2")
    assert os.path.isfile("fubar/foo/bar.txt")
    assert os.path.isfile("fubar/foo/foo2/bar2.txt")
    os.remove("cloudfile.json")
    del_folder("fubar")
