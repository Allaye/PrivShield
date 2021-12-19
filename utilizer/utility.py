import imaplib


class ReplyMsg(imaplib.IMAP4_SSL):
    def __init__(self, imap_server, sender_email, sender_pwd, ssl=None):
        super().__init__(imap_server)
        self.host = imap_server
        self.sender = sender_email
        self.sender_pwd = sender_pwd
        self.ssl = ssl
