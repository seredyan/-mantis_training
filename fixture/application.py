
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):     # запуск браузера через этот конструктор
        self.wd = webdriver.Firefox()
        #self.wd.implicitly_wait(1)
        self.session = SessionHelper(self) # помощник получает ссылку на объект класса Application
                                           # это даст возможность в одном помощнике обращаться к др помощникам
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url     # просим браузер сообщить текущий адрес открытой страницы.
            return True              # если браузер сообщит адрес, то возвращаем True.
        except:
            return False           # значит браузер негоден к исп-ю и фикстура тоже



    def open_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/index.php"):
            wd.get("http://localhost/addressbook/index.php")


    def destroy(self):
        self.wd.quit()

