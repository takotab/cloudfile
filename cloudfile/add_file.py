import os

from .cloudfile import CloudFile


def add_file(file: str, cloudf: CloudFile = None, hard=False):
    if cloudf is None:
        cloudf = CloudFile()
    assert os.path.isfile(file)
    
