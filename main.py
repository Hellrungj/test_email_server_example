from abc import ABC, abstractclassmethod
from dataclasses import dataclass, field
import random
import string
from typing import List


class Email_Address(ABC):
    mail_server: str
    domain: str
    username: str
    _display_name: str

    @abstractclassmethod
    def display_name(self):
        pass

@dataclass
class Owl_Mail(Email_Address):
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

@dataclass
class Email_Server:
    """Creates and Maintains Emails"""
    domain_name: str
    top_level_domain: str
    host: str = "127.0.0.1"
    port: str = "80"
    _email_addresses: dict[Email_Address] = field(init=False, default_factory=dict, repr=False)

    def genrate_email_address(self, username: str, email_type: Email_Address) -> Email_Address:
        """Genrates an Email and adds to the list of email_addresses and returns the email adress that was created"""
        email_address = email_type(mail_server=self.domain_name, domain=self.top_level_domain, username=username)
        self._email_addresses[email_address._display_name] = (email_address)
        return email_address

    @property
    def email_addresses(self) -> List[str]:
        """Returns a list of all the email in the server"""
        email_list: list = []
        for email_address in self._email_addresses.values():
            email_list.append(email_address.display_name)
        return email_list

    def find_email_address(self, username: str) -> Email_Address:
        """Return the email address based by username"""
        return self._email_addresses[username]

@dataclass
class Person:
    """Create a Person with a name, age and email addresses"""
    first_name: str
    last_name: str
    age: int
    _email_addresses: list[Email_Address] = field(default_factory=list, repr=False)

    def add_email_address(self, email_address: Email_Address) -> None:
        """Add an existing email address to person email addresses"""
        self._email_addresses.append(email_address)

    @property
    def full_name(self) -> str:
        """Genrates and return the person's full name"""
        return f"{self.first_name} {self.last_name}"


def main() -> None:
    """This is a Main Function"""
    email_server = Email_Server(domain_name="NoctuaFukuro", top_level_domain="com")
    
    people = [
        Person(first_name="John", last_name="Hellrung", age=27),
        Person(first_name="Chris", last_name="Jansen", age=31)
    ]

    for person in people:
        email_server.genrate_email_address(username=person.full_name, email_type=Owl_Mail)

    print(f"Server Info:\n\t{email_server}")
    print(f"Email Address:\n\t{email_server.email_addresses}")


if __name__ == '__main__':
    main()