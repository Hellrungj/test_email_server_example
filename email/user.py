from email.i_email_address import IEmailAddress

from dataclasses import dataclass, field

@dataclass
class User:
    """Create a Person with a name, age and email addresses"""
    first_name: str
    last_name: str
    age: int
    username: str = field(init=False)
    _email_addresses: list[IEmailAddress] = field(init=False, default_factory=list, repr=False)

    def __post_init__(self) -> None:
        """Sets the username for the user"""
        self.username = f"{self.first_name}.{self.last_name}"

    def add_email_address(self, email_address: IEmailAddress) -> None:
        """Add an existing email address to person email addresses"""
        self._email_addresses.append(email_address)

    @property
    def full_name(self) -> str:
        """Genrates and return the person's full name"""
        return f"{self.first_name} {self.last_name}"