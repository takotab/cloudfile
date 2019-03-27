import os

from tests.utils import ini_files, del_folder

import cloudfile


def test_make_cloudfile():
    if os.path.isfile(".clouldfile"):
        os.remove(".cloudfile")
    del_folder("foo")

    ini_files({"foo": ["bar.txt", {"foo2": "bar2.txt"}]})
    cloudfile.save(
        "foo",
    )

    assert os.path.isfile(".cloudfile")
    os.remove(".cloudfile")
    del_folder("foo")
