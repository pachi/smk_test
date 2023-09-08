import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "mylib"))

import mylib

mylib.hello()