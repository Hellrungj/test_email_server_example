from email.i_email_address import IEmailAddress

import random
import string
from dataclasses import dataclass, field

@dataclass
class OwlMail(IEmailAddress):
    """Create an Email Adress"""
    mail_server: str
    domain: str
    username: str = field(default_factory="".join(random.choices(string.ascii_uppercase, k=12)))
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

    def __str__(self) -> str:
        """Displays the display name"""
        return self.display_name