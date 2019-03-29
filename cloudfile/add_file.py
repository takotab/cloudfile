import os

from .cloudfile import CloudFile
from .google import upload_file


def add_file(file: str, cloudf: CloudFile = None, hard=False, unit_test=False):
    if cloudf is None:
        cloudf = CloudFile()
    assert os.path.isfile(file)
    url, file_id = cloudf.upload_file(file)
    if unit_test:
        return cloudf, url, file_id
    return url
