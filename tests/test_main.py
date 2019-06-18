import os
from cloudfile.__main__ import MainCloudFile
from tests.test_restore import create_dct


from tests.utils import ini_files, del_folder


def test_main(monkeypatch):
    create_dct()
    cfile = MainCloudFile()
    cfile.restore()
    cfile.download("foo/bar.txt")
    os.remove("foo/bar.txt")


def test_restore_file(monkeypatch):
    create_dct()
    cfile = MainCloudFile()
    cfile.restore_file("foo/bar.txt")
    os.remove("foo/bar.txt")


def test_main_add_file_del(monkeypatch):
    create_dct()
    cfile = MainCloudFile()
    cfile.add_link("foo/fubar.txt", "google.com")

    monkeypatch.setattr("builtins.input", lambda: "Y")
    cfile.del_link("foo/fubar.txt")


def test_main_add_folder_del(monkeypatch):
    create_dct()  # TODO check if already in dict and use hard
    ini_files({"foo": ["bar.txt", "bar3.txt", {"foo2": "bar2.txt"}]})
    cfile = MainCloudFile()
    cfile.add("foo")

    monkeypatch.setattr("builtins.input", lambda: "Y")
    cfile.del_link("foo/bar3.txt")
