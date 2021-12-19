import imaplib


class ReplyMsg(imaplib.IMAP4_SSL):

    def __init__(self, host):
        super(ReplyMsg, self).__init__(host)

    def signout(self):
        try:
            return self.logout()
        except Exception as e:
            return e

    def login(self, email: str, pwd: str):
        try:
            return self.login(email, pwd)
        except Exception as e:
            return e



