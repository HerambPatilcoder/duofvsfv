

import os
import sys

def check_directory(dir):
    total_files = 0
    total_size = 0
    for root, dirs, files in os.walk(dir):
        for file in files:
            fpath = os.path.join(root,file)

            total_size += os.path.getsize(fpath)
            total_files += 1
    print(total_size)
    print(total_files)

    items = [os.path.join(dir,name) for name in os.listdir(dir)]
    contents = sorted(items, key=os.path.getmtime)

    
   

for directory in sys.argv[1:]:
    check_directory(directory)