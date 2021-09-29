

from selenium import webdriver
from fixture.session import SessionHelper
from fixture.projects import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper


class Application:

    def __init__(self, browser, config):     # запуск браузера через этот конструктор
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd.webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self) # помощник получает ссылку на объект класса Application
                                           # это даст возможность в одном помощнике обращаться к др помощникам


        self.james = JamesHelper(self)
        self.project = ProjectHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']




    def is_valid(self):
        try:
            self.wd.current_url     # просим браузер сообщить текущий адрес открытой страницы.
            return True              # если браузер сообщит адрес, то возвращаем True.
        except:
            return False           # значит браузер негоден к исп-ю и фикстура тоже



    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)



        # if not wd.current_url.endswith("/index.php"):
        #     wd.get("http://localhost/addressbook/index.php")


    def destroy(self):
        self.wd.quit()

