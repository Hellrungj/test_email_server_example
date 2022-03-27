from dataclasses import dataclass, field
import random
import string

from email_server.i_email_address import IEmailAddress

def genrate_random_username() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

@dataclass
class OwlMail(IEmailAddress):
    """Create an Email Adress"""
    mail_server: str
    domain: str
    username: str = field(default_factory=genrate_random_username)
    _display_name: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        """Sets the _Display_Name for the email address"""
        self._display_name = f"{self.username}@{self.mail_server}.{self.domain}"

    @property
    def display_name(self) -> str:
        """Sets Display Name as a property"""
        return self._display_name

    def genrate_username(self, first_name: str, last_name: str) -> None:
        """Genrates a username using a first and last name"""
        self.username = f"{first_name}.{last_name}"
        self._display_name = f"{self.username}@{self.mail_server}.{self.domain}"

    def __str__(self) -> str:
        """Displays the display name"""
        return self.display_name