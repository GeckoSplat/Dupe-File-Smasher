from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import hashlib
from send2trash import send2trash



Tk().withdraw() # Don't need full GUI, so stops root window from appearing 
path = askdirectory (title = 'Please Select A Folder')

def smash_dupe_files():
    walker1 = os.walk(path, topdown=False)
    uniqueFiles = dict()
    for folder, sub_folder, files in walker1:
        print (f'{files,folder}')
        for file in files:
            filepath = os.path.join(folder,file)
            filehash = hashlib.md5(open(filepath,'rb').read()).hexdigest()
            if filehash in uniqueFiles:
                send2trash(filepath)
                print (f'{filepath} Has Been Deleted')
            else:
                uniqueFiles[filehash] = path
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)
            print(f'{folder} Has Been Deleted ')
  

        

if  __name__ == '__main__':
    smash_dupe_files()
    
    print ('\n\tOperation complete. Please check recycle bin for deleted data before permenant removal')