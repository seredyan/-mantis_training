

import random
import string
import os.path
import json
from model.project import Project
import getopt
import sys
import re

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
    pass