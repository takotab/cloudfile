import os
import cloudfile
from cloudfile.google import delete_google_file
from tests.utils import del_folder


def test_add_file():
    if not os.path.isdir("foo"):
        os.mkdir("foo")
    filename = "foo/bar_new.txt"
    with open(filename, "w") as f:
        f.write("hello world")
    cloudf, url, file_id = cloudfile.add_file(filename, unit_test=True)
    os.remove(filename)
    cloudfile.download(filename, url)
    assert os.path.isfile(filename)
    delete_google_file(cloudf.service, file_id)
    del_folder("foo")


def test_add_file_wo_folder():
    filename = "foobar.txt"
    with open(filename, "w") as f:
        f.write("hello world")
    cloudf, url, file_id = cloudfile.add_file(filename, unit_test=True)
    os.remove(filename)
    cloudfile.download(filename, url)
    assert os.path.isfile(filename)
    delete_google_file(cloudf.service, file_id)
    os.remove(filename)

