from typing import List
from email.email_server import EmailServer
from email.owl_mail import OwlMail
from email.user import User

def main() -> None:
    """This is a Main Function"""
    email_server: EmailServer = EmailServer(domain_name="NoctuaFukuro", top_level_domain="com")
    
    users: List[User] = [
        User(first_name="John", last_name="Hellrung", age=27),
        User(first_name="Chris", last_name="Jansen", age=31)
    ]

    user: User
    for user in users:
        email_server.genrate_email_address(username=user.username, email_type=OwlMail)

    print(f"Server Info:\n\t{email_server}")
    print(f"Email Address:\n\t{email_server.email_addresses}")


if __name__ == '__main__':
    main()