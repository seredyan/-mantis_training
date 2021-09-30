


def test_to_homework_26(app):
    assert app.soap.get_projects_list(username="administrator", password="root")
