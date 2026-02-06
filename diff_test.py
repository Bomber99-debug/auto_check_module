from operator import index
from sys import argv
from pathlib import Path
from itertools import zip_longest

if len(argv) != 3:
    print("Please provide for two files")
    exit()

item_one_path, item_two_path = argv[1:]

item_one = Path(item_one_path)
item_two = Path(item_two_path)

if item_one.is_dir() and item_two.is_dir():
    print(f"Both paths {item_one} and {item_two} are folders")

if item_one.is_dir():
    print(f'{item_one} is a folder')
    exit()

if item_two.is_dir():
    print(f'{item_two} is a folder')
    exit()

with open(item_one) as file_one:
    file_one_lines = file_one.readlines()

with open(item_two) as file_two:
    file_two_lines = file_two.readlines()

for index, (one_lines, two_lines) in enumerate(zip_longest(file_one_lines, file_two_lines, fillvalue="No element")):
    if one_lines != two_lines:
        print(index + 1)
        print(f"> {one_lines.rstrip()}")
        print(f"< {two_lines.rstrip()}")