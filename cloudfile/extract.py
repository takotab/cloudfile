import os


def extract(file: str):
    if file[-3:] == ".7z":
        os.system("7z x " + file)
    

