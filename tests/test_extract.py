import os

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
