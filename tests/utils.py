import glob
import os


def ini_files(folders: dict, root=""):
    for key, item in folders.items():
        os.mkdir(os.path.join(root, key))
        if type(item) == dict:
            ini_files(item, root=os.path.join(root, key))
        elif type(item) == str:
            with open(item, "w") as f:
                f.write("foo bar")


def del_folder(folder: str, glob_pattern="*"):
    if not os.path.exists(folder):
        return
    for f in glob.glob(os.path.join(folder, glob_pattern)):
        if os.path.isdir(f):
            del_folder(f)
        else:
            os.remove(f)
    try:
        os.removedirs(folder)
    except:
        pass
