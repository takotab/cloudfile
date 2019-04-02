import os


def extract(file: str):
    if file[-3:] == ".7z":
        if in_subfolder(file):
            os.system("7z x " + file + " -oc:" + os.path.join(*file.split(os.sep)[:-1]))
        else:
            os.system("7z x " + file)


def in_subfolder(file):

    spllitted = file.split(os.sep)[:-1]
    if len(spllitted) == 0:
        return False
    if len(spllitted) > 1:
        return True

    if spllitted != ["."]:
        return True
    return False
