import os


def file_downloaded(file_dir: str):
    with open(file_dir, "r") as f:
        line = f.readline()
        if "<title>Google Drive - Virus scan warning</title>" in line:
            return False

    return True
