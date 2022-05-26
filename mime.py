# For MIME types
import magic
import os
from tkinter import Tk
from tkinter import filedialog
Tk().withdraw()
path = filedialog.askdirectory()
path=path+"/"
# print(path)

mime = magic.Magic(mime=True)
directory = path
mime_type=str(input("Enter the MIME type to want to filter, For Example (application/pdf): "))
for filename in os.listdir(directory):
    print(filename)
    try:
        if(mime.from_file(path+filename)) == mime_type:
            pass
        else:
            os.remove(os.path.join(directory, filename))
    except:
        os.remove(os.path.join(directory, filename))

