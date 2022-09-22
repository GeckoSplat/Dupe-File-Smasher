from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import hashlib
from send2trash import send2trash

Tk().withdraw() # Don't need full GUI, so stops root window from appearing 
path = askdirectory (title = 'Please Select A Folder')

walker = os.walk(path)
uniqueFiles = dict()
for folder, sub_folder, files in walker:
    for file in files:
        filepath = os.path.join(folder,file)
        filehash = hashlib.md5(open(filepath,'rb').read()).hexdigest()
        if filehash in uniqueFiles:
            send2trash(filepath)
            print (f'{filepath} Has Been Deleted')
        else:
            uniqueFiles[filehash] = path   
