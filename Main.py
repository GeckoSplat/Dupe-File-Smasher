from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import os
import hashlib
from send2trash import send2trash


Tk().withdraw()
path = askdirectory(title="Please Select A Folder To Smash")


def smash_dupe_files():
    walker1 = os.walk(path, topdown=False)
    uniqueFiles = dict()
    # sub_folder needs to be present or not enought values to unpack creates a Value Error.
    for folder, sub_folder, files in walker1:
        for file in files:
            filepath = os.path.join(folder, file)
            filehash = hashlib.md5(open(filepath, "rb").read()).hexdigest()
            if filehash in uniqueFiles:
                send2trash(filepath)
                print(f"{filepath} Has Been Deleted")
            else:
                uniqueFiles[filehash] = path
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)
            print(f"{folder} Has Been Deleted ")


def message():
    messagebox.showinfo(
        title="File Smasher Done", message="Please check recycle bin for deleted data"
    )


if __name__ == "__main__":

    try:
        smash_dupe_files()
        message()
        print("\n\tOperation complete. \n\tPlease check recycle bin for deleted data.")
    except TypeError:
        print("\n\tRun Cancelled.")
        exit()
