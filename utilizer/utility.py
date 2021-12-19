import re
import imaplib


class ReplyMsg(imaplib.IMAP4_SSL):
    """
    *************************
    """
    def __init__(self, host):
        super().__init__(host)

    def logout(self):
        try:
            return super().logout()
        except Exception as e:
            return e

    def login(self, email: str, pwd: str):
        try:
            return super().login(email, pwd)
        except Exception as e:
            return e

    def list_folder_label(self):
        labels = self.list()[1]
        return [re.findall(r'"([^"]*)"', l.decode("UTF-8"))[-1] for l in labels]



