import os
import cloudfile
from tests.utils import del_folder


def test_add_file():
    if not os.path.isdir("foo"):
        os.mkdir("foo")
    filename = "foo/bar_new.txt"
    with open(filename, "w") as f:
        f.write("hello world")
    url = cloudfile.add_file(filename)
    os.remove(filename)
    cloudfile.download(filename, url)
    assert os.path.isfile(filename)
    del_folder("foo")

