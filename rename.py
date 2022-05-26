import os, sys
import hashlib
from tkinter import Tk
from tkinter import filedialog 

def md5(fileName):
    m=hashlib.md5()
    try:
        fd = open(fileName,"rb")
    except IOError:
            print(" Unable to open the file in readmode: ",fileName)
            return
    content = fd.read()
    fd.close()
    m.update(content)

    return m.hexdigest()

Tk().withdraw()
path = filedialog.askdirectory()
path=path+"/"
# print(path)
list = os.listdir(path)
extension=str(input("Enter the extension you want to rename files in, For Example(.txt): "))

for f in list:
    ao=os.path.join(path, f)
    md5sum = md5(ao)
    filename = ao
    new_filename = path+md5sum+extension
    os.rename (filename,new_filename)
    print('Renamed'+filename+' to '+new_filename)
