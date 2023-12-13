### name.py

import sys

if len(sys.argv) < 2:
    sys.exit("Too Few Args")
elif len(sys.argv) > 2:
    sys.exit("Too Many Args")

print("Hell, my name is", sys.argv[1])
