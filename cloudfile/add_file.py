import os

from .cloudfile import CloudFile
from .google_drive import upload_file


def add_file(file: str, cloudf: CloudFile = None, hard=False):
    if cloudf is None:
        cloudf = CloudFile()
    assert os.path.isfile(file)
    return cloudf.upload_file(file)
