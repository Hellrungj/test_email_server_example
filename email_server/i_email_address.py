from abc import ABC, abstractclassmethod

class IEmailAddress(ABC):
    mail_server: str
    domain: str
    username: str
    _display_name: str

    @abstractclassmethod
    def display_name(self):
        pass