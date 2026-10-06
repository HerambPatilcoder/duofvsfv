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

import pandas as pd

new_path = "/Users/herambpatil/Documents/cs699/assign2/students.csv"
csv_ = pd.read_csv(new_path)

if os.path.exists(new_path):
    print(csv_.shape[0])
    df1 = csv_[csv_['Department']=='CSE']
    print(df1.shape[0])
    print(csv_[csv_['Department']=='EE'])


home = os.path.expanduser('~')
item = []
for name in os.listdir(home):
    path = os.path.join(home,name)
    if os.path.islink(path):
        continue
    try:
        if os.path.isfile(path):
            size = os.path.getsize(path)
        elif os.path.isdir(path):
            size=0
            for root, dirs, files in os.walk(path):
                dirs[:] = [d for d in dirs if not os.path.islink(os.path.join(root,d))]
                for file in files:
                    fpath = os.path.join(root,file)
                    if not os.path.islink(fpath) and os.path.isfile(fpath):
                        try:
                            size += os.path.getsize(fpath)
                        except(FileNotFoundError):
                            continue    
        items.append(size,path)
    except(PermissionError, FileNotFoundError):
        continue

items.sort(reverse=True)
for size, path in items[:10]:
    print(f"{size / (1024**2):.1f}M\t{path}")





