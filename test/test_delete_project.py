import random
from model.project import Project



def test_delete_project_assert_ui(app):
    if app.soap.get_projects_list(username="administrator", password="root") == []:
        app.project.create_project(Project(name='test_project', description='some text'))

    old_projects = app.soap.get_projects_list(username="administrator", password="root")
    deletable_project = random.choice(old_projects)
    app.project.delete_project(old_projects.index(deletable_project))
    new_projects = app.soap.get_projects_list(username="administrator", password="root")
    old_projects.remove(deletable_project)

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)





# def test_delete_project_assert_ui(app):
#     if app.project.get_project_list() == []:
#         app.project.create_project(Project(name='test_project', description='some text'))
#
#     old_projects_ui = app.project.get_project_list()
#     deletable_project = random.choice(old_projects_ui)
#     app.project.delete_project(old_projects_ui.index(deletable_project))
#     new_projects_ui = app.project.get_project_list()
#     old_projects_ui.remove(deletable_project)
#
#     assert sorted(old_projects_ui, key=Project.id_or_max) == sorted(new_projects_ui, key=Project.id_or_max)



