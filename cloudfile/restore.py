import os
import json
import wget

from .cloudfile import CloudFile


def restore(cloudf: CloudFile = None, hard=False):
    if cloudf is None:
        cloudf = CloudFile()
    for dir, url in cloudf.items():
        path_to = get_path_to(dir)
        if not os.path.isdir(path_to):
            os.mkdir(path_to)
        if not os.path.isfile(dir) or hard:
            download(dir, url)
        else:
            print(
                f"Did not download {dir}. File already exist.\nRun `cloudfile download {dir}` to download this file anyway."
            )


def download(dir: str, url: str):
    path_to = get_path_to(dir)
    wget.download(url, out=path_to)
    print(f"Downloaded {dir} from {url}")


def get_path_to(path: str):
    return os.path.join(*path.split(os.sep)[:-1])
