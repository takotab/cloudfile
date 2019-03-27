import os

from .cloudfile import CloudFile


def save(dir: str):
    cloudf = CloudFile()
    if os.path.isfile(dir):
        cloudf.save_file(dir)
        return
    assert os.path.isdir(dir)
    for item in os.listdir(dir):
        save(os.path.join(dir, item))

