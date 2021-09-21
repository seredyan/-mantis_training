import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type='submit']").click()
        # wd.find_element_by_xpath("//input[@value='Login']").click()


    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        #wd.find_element_by_name("user")   # можно добавить это, чтобы полноценно произошел logout
                                          # и найден "user" для нового входа

    def is_logged_in(self):
        wd = self.app.wd
        time.sleep(0.2)  # добавлено ожидание, чтобы открылась главная страница до начала поиска элемента "Logout"-??
        return len(wd.find_elements_by_link_text("Logout")) > 0


    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]  # находит имя пользователя и отрезает у него круглые скобки у "("+username+")"

        # return wd.find_element_by_xpath("//div[@id='top']/form/b").text == "(%s)" % username   # альтернатива:  ...text == "("+username+")"
        # return wd.find_element_by_xpath("//div/div[1]/form/b").text == "(%s)" % username
        # return wd.find_element_by_xpath("//*[@id='top']/form/b").text == "(%s)" % username
        # return wd.find_element_by_xpath("//b[contains(.,'(admin)')]").text == % username




    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()



    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

