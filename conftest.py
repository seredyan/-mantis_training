

from fixture.application import Application
import pytest
import json
import os.path
import ftputil
import importlib
import jsonpickle




fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as fl:
            target = json.load(fl)
    return target


@pytest.fixture(scope="session")  # эта фикстура для исп другими фискстурами (zB for configure_server)
def config(request):
    return load_config(request.config.getoption("--target"))



@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    # web_config = load_config(request.config.getoption("--target"))['web']
    webadmin_config = load_config(request.config.getoption("--target"))['webadmin']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, config=config)
        # fixture.session.login(usename=config['webadmin']['username'], password=config['webadmin']['password'])
        fixture.session.login(username=webadmin_config['username'], password=webadmin_config['password'])
    # fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)     # ролик 9_2
def configure_server(request, config):
    install_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password']) # по протоколу ftp подложить нужный конфигурационный файл на сервер

    def fin(): # цель - восстановить конфигурацию с сервера
        restore_install_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])

    request.addfinalizer(fin)


def install_server_configuration(host, username, password):  # ролик 9_2
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            remote.remove("config_inc.php.bak")
        if remote.path.isfile("config_inc.php"):
            remote.rename("config_inc.php", "config_inc.php.bak")
        remote.upload(os.path.join(os.path.dirname(__file__), "resources/config_inc.php"), "config_inc.php")




def restore_install_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            if remote.path.isfile("config_inc.php"):
                remote.remove("config_inc.php")
            remote.rename("config_inc.php.bak", "config_inc.php")



@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture




def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")




#
#
# def pytest_generate_tests(metafunc):
#     for fixture in metafunc.fixturenames:
#         if fixture.startswith("data_"):
#             testdata = load_from_module(fixture[2:]) # удаляем первые 5 символов из (???)загруженных данных (????)
#             metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
#         elif fixture.startswith("json_"):
#             testdata = load_from_json(fixture[2:])  # удаляем первые 5 символов из (???)загруженных данных (????)
#             metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
#
#
#
# def load_from_module(module):
#     return importlib.import_module("data.%s" % module).testdata
# #
# #
# def load_from_json(file):
#     with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
#         return jsonpickle.decode(f.read())
# #
# #













###***********************
# ниже вариант к заданию 25


# fixture = None
# target = None
#
#
# def load_config(file):
#     global target
#     if target is None:
#         config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
#         with open(config_file) as f:
#             target = json.load(f)
#     return target
#
#
# @pytest.fixture
# def app(request):
#     global fixture
#     browser = request.config.getoption("--browser")
#     web_config = load_config(request.config.getoption("--target"))['web']
#     webadmin_config = load_config(request.config.getoption("--target"))['webadmin']
#     if fixture is None or not fixture.is_valid():
#         fixture = Application(browser=browser, base_url=web_config['baseUrl'])
#         fixture.session.login(username=webadmin_config['username'], password=webadmin_config['password'])
#     return fixture
#
#
#
# @pytest.fixture(scope="session", autouse=True)
# def stop(request):
#     def fin():
#         fixture.session.logout()
#         fixture.destroy()
#     request.addfinalizer(fin)
#     return fixture
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="firefox")
#     parser.addoption("--target", action="store", default="target.json")
#
#

































