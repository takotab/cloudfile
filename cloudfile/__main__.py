# __main__.py
import os

import fire

from .ask_confermation import query_yes_no
from .restore import restore, download as file_download
from .cloudfile import CloudFile
from .add_file import add_file as google_add_file
from .add_file import add as google_add


class MainCloudFile(object):
    def __init__(self,):
        self.cloudf = CloudFile()

    def restore(self, hard=False):
        """This will restore the keys with the corresponding urls in `cloudfile.json`"""
        restore(self.cloudf, hard)

    def add_file(self, file, hard=False):
        """Uploud the file to google drive and adds the link to `cloudfile.json`"""
        google_add_file(file, self.cloudf, hard=hard)

    def add(self, dir, hard=False):
        """Uploud file or the content of the folder to google drive and adds the link to `cloudfile.json`"""
        google_add(dir, self.cloudf, hard=hard)

    def add_link(self, file, link):
        """Add a link to `cloudfile.json`"""
        self.cloudf.dct[file] = link
        if not os.path.isfile(file):
            Warning(f"{file} does not exist.")
        self.cloudf.save_json()
        print(f"{file} added to `cloudfile.json`")

    def del_link(self, file):
        """Delete a link from `cloudfile.json`"""
        if query_yes_no(f"Are you sure you want to delete {file}?"):
            del self.cloudf.dct[file]
            self.cloudf.save_json()
            print(f"{file} has been removed of `cloudfile.json`")

    def download(self, file):
        """Download the file even if the file already exists."""
        url = self.cloudf[file]
        file_download(file, url)

    # def add(self, dir):


if __name__ == "__main__":
    fire.Fire(MainCloudFile)
