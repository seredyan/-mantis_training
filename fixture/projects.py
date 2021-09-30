import random

from selenium.webdriver.support.ui import Select
import time
from model.project import Project




class ProjectHelper:
    def __init__(self, app):
        self.app = app




    def create_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        time.sleep(0.5)
        self.fill_project_creatings_fields(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        wd.implicitly_wait(1)
        self.project_cache = None




    def delete_project(self, index):
        wd = self.app.wd
        # self.open_projects_page()
        self.select_deletable_project(index)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        time.sleep(1)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.project_cache = None

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []

            all_projects = wd.find_elements_by_css_selector("tr.row-1 a, tr.row-2 a")

            for project in all_projects:
                id = (project.get_attribute('href')).split("id=",1)[1]
                name = project.text

                self.project_cache.append(Project(id=id, name=name))

        return list(self.project_cache)



    def select_deletable_project(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector("tr.row-1 a, tr.row-2 a")[index].click()






    def fill_project_creatings_fields(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        time.sleep(0.5)
        self.change_field_value("description", project.description)
        time.sleep(0.2)

        element = wd.find_element_by_name("status")
        all_options = element.find_elements_by_tag_name("option")
        random.choice(all_options).click()

        Select(wd.find_element_by_name("view_state")).select_by_value('50')





    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)



    def open_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_overview_page.php"):
            self.app.open_home_page()
        wd.find_element_by_link_text("Manage").click()
        time.sleep(0.5)
        wd.find_element_by_link_text("Manage Projects").click()
        time.sleep(0.5)
