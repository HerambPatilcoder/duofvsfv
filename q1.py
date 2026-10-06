import os
import time

project = "/Users/herambpatil/Documents/cs699/assign2/yo"

total_files = 0
total_size = 0
if os.path.exists(project):
    for root,dirs,files in os.walk(project):
        for file in files:
            fpath = os.path.join(root,file)

            total_files+=1
            total_size += os.path.getsize(fpath)

    items = sorted(os.scandir(project), key=lambda entry: entry.stat().st_mtime)

    print(total_size)
    print(total_files)

    for entry in items:
        mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(entry.stat().st_mtime))
        size = entry.stat().st_size
        print(f"{mtime}\t{size:>8} B\t{entry.name}")
