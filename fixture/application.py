

from selenium import webdriver
from fixture.session import SessionHelper
from fixture.projects import ProjectHelper


class Application:

    def __init__(self, browser, base_url):     # запуск браузера через этот конструктор
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd.webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self) # помощник получает ссылку на объект класса Application
                                           # это даст возможность в одном помощнике обращаться к др помощникам

        self.base_url = base_url
        self.project = ProjectHelper(self)




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

