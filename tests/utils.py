import glob
import os


def ini_files(folders: dict, root: str = ""):
    del_folder(list(folders.keys())[0])
    for key, item in folders.items():
        os.mkdir(os.path.join(root, key))
        curr_root = os.path.join(root, key)
        if type(item) == dict:
            ini_files(item, root=curr_root)
        elif type(item) == list:
            handle_lists(item, root=curr_root)
        elif type(item) == str:
            make_file(item, root=curr_root)


def handle_lists(dir_lst: list, root: str):
    for dir in dir_lst:
        if type(dir) == dict:
            ini_files(dir, root)
        elif type(dir) == str:
            make_file(dir, root)
        elif type(dir) == list:
            handle_lists(dir, root)


def make_file(f_name: str, root: str):
    with open(os.path.join(root, f_name), "w") as f:
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
