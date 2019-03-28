from cloudfile.__main__ import MainCloudFile
from tests.test_restore import create_dct


def test_main(monkeypatch):
    create_dct()
    cfile = MainCloudFile()
    cfile.restore()
    cfile.download("foo/bar.txt")


def test_main_add_del(monkeypatch):
    create_dct()
    cfile = MainCloudFile()
    cfile.add_link("foo/fubar.txt", "google.com")

    monkeypatch.setattr("builtins.input", lambda: "Y")
    cfile.del_link("foo/fubar.txt")
