import os

home = os.path.expanduser("~")
items = []

for name in os.listdir(home):
    path = os.path.join(home, name)
    if os.path.islink(path):
        continue

    try:
        if os.path.isfile(path):
            size = os.path.getsize(path)
        elif os.path.isdir(path):
            size = 0
            for root, dirs, files in os.walk(path, followlinks=False):
                dirs[:] = [d for d in dirs if not os.path.islink(os.path.join(root, d))]
                for f in files:
                    fpath = os.path.join(root, f)
                    if not os.path.islink(fpath) and os.path.isfile(fpath):
                        try:
                            size += os.path.getsize(fpath)
                        except (PermissionError, FileNotFoundError):
                            continue
        items.append((size, path))
    except (PermissionError, FileNotFoundError):
        continue

items.sort(reverse=True)

print("\nTop 10:")
for size, path in items[:10]:
    print(f"{size / (1024**2):.1f}M\t{path}")