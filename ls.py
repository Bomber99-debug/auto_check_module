# sys.exit
# sys.argv

import sys
from pathlib import Path
from colorama import Fore, Style


folder_path = "." if len(sys.argv) != 2 else sys.argv[1]


p = Path(folder_path)

dir_list = ''
file_dir = ''

p_dir = [f"{Fore.BLUE}{str(x)}/{Style.RESET_ALL}" if x.is_dir() else f"{Fore.GREEN}{x}{Style.RESET_ALL}" for x in p.iterdir()]

for x in p_dir:
    print(x)