from email.i_email_address import IEmailAddress

from typing import List
from dataclasses import dataclass, field

@dataclass
class EmailServer:
    """Creates and Maintains Emails"""
    domain_name: str
    top_level_domain: str
    host: str = "127.0.0.1"
    port: str = "80"
    _email_addresses: dict[IEmailAddress] = field(init=False, default_factory=dict, repr=False)

    def genrate_email_address(self, username: str, email_type: IEmailAddress) -> IEmailAddress:
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

    def find_email_address(self, username: str) -> IEmailAddress:
        """Return the email address based by username"""
        return self._email_addresses[username]