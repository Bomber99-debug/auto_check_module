from pathlib import Path
from sys import argv, exit


# item_path = "." if len(argv) != 2 else argv[1]

if len(argv) != 2:
    print("Please provide a file path")
    exit()

item_path = argv[1]

item = Path(item_path)

if item.is_dir():
    print(f'{item} is a folder')
    exit()

with open(item_path) as file:
    for i in file:
        print(i)