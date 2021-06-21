import os
import time
from keyvault import secrets_to_environment
import pytest
from notify import NotifyMail
from notify.tests import import_sample_dfs
from notify.exceptions import DataFrameTooLarge

secrets_to_environment("notify")


def test_send_single_email():
    message = "This is a test from notify"
    NotifyMail(
        to=f"{os.environ.get('TEST_EMAIL_1')}", subject="Test Notify single email", message=message
    ).send_email()
    time.sleep(2)


def test_send_email_with_table():
    message = "This is a test from notify"
    df = import_sample_dfs().get("Metadata")

    NotifyMail(
        to=f"{os.environ.get('TEST_EMAIL_1')}",
        subject="Test Notify single email",
        message=message,
        df=df,
    ).send_email()
    time.sleep(2)


def test_send_email_with_too_large_table():
    message = "This is a test from notify"
    df = import_sample_dfs(transactions=35).get("Transactions")

    with pytest.raises(DataFrameTooLarge):
        NotifyMail(
            to=f"{os.environ.get('TEST_EMAIL_1')}",
            subject="Test Notify single email",
            message=message,
            df=df,
        ).send_email()

    time.sleep(2)


def test_send_multiple_emails():
    message = "This is a test from notify"
    NotifyMail(
        to=f"{os.environ.get('TEST_EMAIL_1')}, {os.environ.get('TEST_EMAIL_2')}",
        subject="Test Notify multiple emails",
        message=message,
    ).send_email()
    time.sleep(2)


def test_send_file():
    message = "This is a test from notify"
    subject = "Test Notify file"
    NotifyMail(
        to=f"{os.environ.get('TEST_EMAIL_1')}",
        subject=subject,
        message=message,
        files=os.path.join("notify", "tests", "data", "2010 car efficiency.csv"),
    ).send_email()


if __name__ == "__main__":
    # test_send_single_email()
    # test_send_multiple_emails()
    test_send_email_with_too_large_table()
