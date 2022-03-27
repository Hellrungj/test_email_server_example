from email_server.i_email_address import IEmailAddress
from email_server.owl_mail import OwlMail
from email_server.user import User

def test_user():
    user = User(first_name="John", last_name="Doe", age=20)

    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.age == 20
    assert user.username == "John.Doe"
    assert user._email_addresses == []

def test_add_email_address():
    user = User(first_name="John", last_name="Doe", age=20)
    email_address: IEmailAddress = OwlMail(mail_server="Example", domain="com", username=user.username)
    user.add_email_address(email_address)

    assert email_address in user._email_addresses

def test_full_name_property():
    user = User(first_name="John", last_name="Doe", age=20)

    assert user.full_name == "John Doe"