from email_server.i_email_address import IEmailAddress
from email_server.owl_mail import OwlMail

def test_genrate_owl_mail_email_address():
    """Created a new Owl Mail Email Address and asserts it's attributes"""
    email_address: IEmailAddress = OwlMail(mail_server="Example", domain="com", username="test")

    assert email_address.mail_server == "Example"
    assert email_address.domain == "com"
    assert email_address.username == "test"
    assert email_address._display_name == "test@Example.com"

def test_display_name_property():
    """"""
    email_address: IEmailAddress = OwlMail(mail_server="Example", domain="com", username="test")

    assert email_address.display_name == "test@Example.com"

def test_genrate_username():
    """"""
    email_address: IEmailAddress = OwlMail(mail_server="Example", domain="com")
    email_address.genrate_username(first_name="john", last_name="doe")

    assert email_address.username == "john.doe"
    assert email_address.display_name == "john.doe@Example.com"
