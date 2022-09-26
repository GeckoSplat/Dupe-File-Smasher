# Dupe-File-Smasher
---
## Small Script for Deleting Duplicate Files.
---
This script will create a window which allows you to choose where in your directory you want it to run. It will then walk the directory from the bottom up deleting duplicate files, leaving only one of each unique file it finds. If this process empties a folder, the folder will also be deleted to keep the directory tidy. 

**The script utilises the Send2Trash library. This means any files deleted will be sent to your recycle bin.**

The only thing deleted permenantly are any empty folders it finds. You can then choose to empty the recycle bin to permenantly delete files.

---
**Prerequisits:**

Install Send2Trash.

Open a terminal window and type the command "pip install send2trash"

Clone / Download this repo.

**Usage**

Open a terminal in the directory where you cloned the repo.

Type " Python ( or Python3 ) Main.py " Press the return key.

Select the directory you wish to run in, in the pop up messagebox. 

Click OK in the messagebox. 

Duplicate files will be put in the recycle bin. 





