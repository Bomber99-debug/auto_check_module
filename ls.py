# sys.exit
# sys.argv

import sys
from pathlib import Path


folder_path = "." if len(sys.argv) != 2 else sys.argv[1]


p = Path(folder_path)

print([x for x in p.iterdir() if x.is_dir()])