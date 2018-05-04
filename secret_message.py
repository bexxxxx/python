#!python2

import os

def rename_files():
    #get file names
    file_list = os.listdir("/Users/RebeccaReilly/github/Python/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current WD is "+saved_path)
    os.chdir("/Users/RebeccaReilly/github/Python/prank")
    #rename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    #change path back to how it was found
    os.chdir(saved_path)
    
rename_files()
