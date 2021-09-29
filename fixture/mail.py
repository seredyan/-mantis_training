
import poplib
import email
import time
import quopri


class MailHelper:   ## video 9_4

    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password, subject):
        for i in range(5):
            pop = poplib.POP3(self.app.config['james']['host'])
            pop.user(username)
            pop.pass_(password)
            num = pop.stat()[0] ## показывет статистику, что есть в почтовом ящике (первый эдемент кортежа - это количество писем)
            if num > 0:
                for n in range(num):
                    msglines = pop.retr(n+1) [1]
                    msgtext = "\n".join(map(lambda x: x.decode('utf-8'), msglines))
                    msg = email.message_from_string(msgtext)
                    if msg.get("Subject") == subject:
                        pop.dele(n+1)
                        pop.quit()
                        return msg.get_payload()

            pop.quit()
            time.sleep(3)

        return None









