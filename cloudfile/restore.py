import os
import json
import wget

from .cloudfile import CloudFile


def restore():
    cloudf = CloudFile()
    for dir, url in cloudf.items():
        path_to = get_path_to(dir)
        os.mkdir(path_to)
        wget.download(url, out=path_to)


def get_path_to(path: str):
    return os.path.join(*path.split(os.sep)[:-1])
