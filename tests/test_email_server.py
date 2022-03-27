from typing import List

from email_server.email_server import EmailServer
from email_server.i_email_address import IEmailAddress
from email_server.owl_mail import OwlMail

def test_genrate_email_server():
    """Created a new Email Server and asserts it's attributes"""
    email_server: EmailServer = EmailServer(domain_name="Example", top_level_domain="com")

    assert email_server.domain_name == "Example"
    assert email_server.top_level_domain == "com"
    assert email_server.host == "127.0.0.1"
    assert email_server.port == "80"
    assert email_server._email_addresses == {}
    assert email_server.email_addresses == []

def test_genrate_owl_mail_email_address():
    """Tests the Genrate Email Address Method with Owl Mail Email Address"""
    username: str = "test"

    email_server: EmailServer = EmailServer(domain_name="Example", top_level_domain="com")
    email_address: IEmailAddress = OwlMail(mail_server=email_server.domain_name, domain=email_server.top_level_domain, username=username)
    result: IEmailAddress = email_server.genrate_email_address(username, OwlMail)

    assert result == email_address
    assert result.username in email_server._email_addresses
    assert result == email_server._email_addresses[result.username]

def test_email_addresses_property():
    """Tests the Email Addresses Property"""
    username: str = "test"
    expected_result: List[str] = ["test@Example.com"]

    email_server: EmailServer = EmailServer(domain_name="Example", top_level_domain="com")
    email_server.genrate_email_address(username, OwlMail)

    assert email_server.email_addresses == expected_result

def test_find_email_address():
    """Tests the Find Email Address Method"""
    username: str = "test"

    email_server: EmailServer = EmailServer(domain_name="Example", top_level_domain="com")
    email_address: IEmailAddress =email_server.genrate_email_address(username, OwlMail)

    assert email_server.find_email_address(username) == email_address