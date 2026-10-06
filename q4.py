import os
from collections import Counter

filenames = [
    name
    for root, _, files in os.walk(".")
    for name in files:
    if os.path.isfile(os.path.join(root, name))
]

for name, count in Counter(filenames).items():
    if count > 1:
        print(name)