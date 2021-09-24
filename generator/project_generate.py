

import random
import string
import os.path
import json
from model.project import Project
import getopt
import sys
import re
import jsonpickle



try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/projects.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits *3
    # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10  # добавили спец символы
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Project(name=random_string("Project", 10), description=random_string("describe", 40)) for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as file_out:
    jsonpickle.set_encoder_options("json", indent=2)
    file_out.write(jsonpickle.encode(testdata))
