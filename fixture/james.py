
from telnetlib import Telnet



class JamesHelper:   # video 9_3

    def __init__(self, app):
        self.app = app


    def ensure_user_exists(self, username, password):  # это логин и пароль создаваемого пользователя почты
        james_config = self.app.config['james']
        tl_session = JamesHelper.Telnet_session(
            james_config['host'], james_config['port'], james_config['username'], james_config['password'])
        if tl_session.is_user_registered(username):
            tl_session.reset_password(username, password)
        else:
            tl_session.create_user(username, password)

        tl_session.quit()





    class Telnet_session:
        def __init__(self, host, port, username, password):  # это логин и пароль для доступа к почтовому серверу
            self.telnet = Telnet(host, port, 8)  # цифра - это таймаут ожидания соединения с сервером
            self.read_until("Login id:")
            self.write(username + "\n")
            self.read_until("Password:")
            self.write(password + "\n")
            self.read_until("Welcome root. HELP for a  list of commands")


        def read_until(self, text):
            self.telnet.read_until(text.encode('ascii'), 8)


        def write(self, text):
            self.telnet.write(text.encode('ascii'))




        def is_user_registered(self, username):
            self.write("verify %s\n" % username)
            res = self.telnet.expect([b"exists", b"does not exist"])
            return res[0] == 0  #  т.е если это 0 значит пользователь существует



        def create_user(self, username, password):
            self.write("adduser %s %s\n" % (username, password))
            self.read_until("User %s added" % username)




        def reset_password(self, username, password):
            self.write("setpassword %s %s\n" % (username, password))
            self.read_until("Password for %s reset" % username)





        def quit(self):
            self.write("quit\n")










