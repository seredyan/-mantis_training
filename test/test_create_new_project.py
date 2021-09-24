
from model.project import Project
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_create_project(app):
    added_projects = Project(name=random_string('name', 10), description=random_string('text', 40))
    app.project.create_project(added_projects)
