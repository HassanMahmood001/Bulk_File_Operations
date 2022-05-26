import datetime, os, sys, logging, hashlib
from pathlib import Path
from os import listdir
from os.path import isfile, join
from tkinter import Tk
from tkinter import filedialog
Tk().withdraw()
input_files_path = filedialog.askdirectory()
input_files_path=input_files_path+"/"
input_files = [f for f in listdir(input_files_path) if isfile(join(input_files_path, f))]
input_files = [os.path.join(input_files_path, x) for x in input_files]
inp_dups = {}
unique_inps = {}

def calculate_hash_val(path, block_size=''):
    file = open(path, 'rb')
    hasher = hashlib.md5()
    data = file.read()
    while len(data) > 0:
        hasher.update(data)
        data = file.read()
    file.close()
    return hasher.hexdigest()

def find_unique_files(dic_unique, dict1):
    for key in dict1.keys():
        if key not in dic_unique:
            dic_unique[key] = dict1[key]

def remove_duplicate_files(all_inps ,unique_inps):
    for file_name in all_inps.keys():
        if all_inps[file_name] in unique_inps and file_name!=unique_inps[all_inps[file_name]]:
            os.remove(file_name)
        elif all_inps[file_name] not in unique_inps:
            os.remove(file_name)

def rmv_dup_process(input_files):
    all_inps={}
    for file_path in input_files:
        if Path(file_path).exists():
           files_hash = calculate_hash_val(file_path)
           inp_dups[files_hash]=file_path
           all_inps[file_path] = files_hash
        else:
            print('%s is not a valid path, please verify' % file_path)
            sys.exit()

    find_unique_files(unique_inps, inp_dups)
    print(inp_dups)
    remove_duplicate_files(all_inps, unique_inps)
if __name__ == '__main__':
    datetime1 = datetime.datetime.now()
    rmv_dup_process(input_files)
    datetime2 = datetime.datetime.now()

    print( "processed in",str(datetime2 - datetime1))



