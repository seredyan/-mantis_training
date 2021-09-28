
from model.project import Project
import random
import string
import time


def test_create_project(app):
    old_projects = app.project.get_project_list()
    added_project = Project(name=random_string('name', 10), description=random_string('text', 40))
    app.project.create_project(added_project)
    time.sleep(1)
    new_projects = app.project.get_project_list()
    old_projects.append(added_project)

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)




def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])