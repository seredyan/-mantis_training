import random
from model.project import Project


def test_delete_project(app):
    if app.project.get_project_list() == []:
        app.project.create_project(Project(name='test_project', description='some text'))

    old_projects = app.project.get_project_list()
    deletable_project = random.choice(old_projects)
    app.project.delete_project(old_projects.index(deletable_project))
    new_projects = app.project.get_project_list()
    old_projects.remove(deletable_project)

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)



