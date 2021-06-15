import time
from keyvault import secrets_to_environment
from notify import NotifyMail


secrets_to_environment("notify")


def test_send_single_email():
    message = "This is a test from notify"
    NotifyMail(to="hello@zypp.io", subject="Test Notify single email", message=message).send_email()
    time.sleep(2)


def test_send_multiple_emails():
    message = "This is a test from notify"
    NotifyMail(
        to="hello@zypp.io, erfan@zypp.io", subject="Test Notify multiple emails", message=message
    ).send_email()
    time.sleep(2)


def test_send_file():
    message = "This is a test from notify"
    subject = "Test Notify file"
    NotifyMail(
        to="hello@zypp.io",
        subject=subject,
        message=message,
        files="notify/tests/data/2010 car efficiency.csv",
    ).send_email()


if __name__ == "__main__":
    # test_send_single_email()
    # test_send_multiple_emails()
    test_send_file()
