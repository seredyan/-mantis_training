

from selenium.webdriver.support.ui import Select
import time




class ProjectHelper:
    def __init__(self, app):
        self.app = app




    def create_project(self):
        wd = self.app.wd
        self.app.session.login("administrator", "root")
        self.app.open_home_page()
        wd.find_element_by_link_text("Manage").click()
        time.sleep(1)
        wd.find_element_by_link_text("Manage Projects").click()
        time.sleep(1)
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        time.sleep(1)


