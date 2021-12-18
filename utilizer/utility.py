import imaplib


class Util(imaplib.IMAP4_SSL):
    def __init__(self):
        super().__init__()
