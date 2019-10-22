import os
import json
import wget

from .cloudfile import CloudFile
from .extract import extract
from .check_downloaded import file_downloaded


def restore_file(file: str, cloudf: CloudFile = None, hard=False, verbose=True):
    if cloudf is None:
        cloudf = CloudFile()
    url = cloudf[file]

    path_to = get_path_to(file)
    if not os.path.isdir(path_to):
        os.makedirs(path_to)

    if not os.path.isfile(file) or hard:
        download(file, url, verbose)
    elif verbose:
        print(
            f"Did not download {file}. File already exist.\nRun `cloudfile download {dir}` to download this file anyway."
        )


def restore(cloudf: CloudFile = None, hard=False):
    if cloudf is None:
        cloudf = CloudFile()
    for file in cloudf.keys():
        print(file)
        restore_file(file, cloudf, hard)


def download(dir: str, url: str, verbose: bool = True):
    path_to = get_path_to(dir)
    file_dir = wget.download(url, out=path_to)
    os.rename(src=file_dir, dst=dir)
    extract(file_dir)
    # if not file_downloaded(dir):
    #     raise NotImplementedError("File is not downloaded something went wrong.")
    if verbose:
        print(f"\nDownloaded {dir} from {url}")


def get_path_to(path: str):
    splitted = path.split(os.sep)
    if len(splitted) == 1:
        return "."
    return os.path.join(*splitted[:-1])
