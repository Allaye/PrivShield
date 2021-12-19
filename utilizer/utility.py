import re
import imaplib


class ReplyMsg(imaplib.IMAP4_SSL):
    """
    This is a utility class to help facilitate the reply of email thread
    """
    def __init__(self, host):
        super().__init__(host)
        self.labels = None

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
        self.labels = self.list()[1]
        return [re.findall(r'"([^"]*)"', l.decode("UTF-8"))[-1] for l in self.labels]



