import os
import time
import pytest
from keyvault import secrets_to_environment
from msgraph.generated.models.o_data_errors.o_data_error import ODataError
from notify import NotifyMail, format_numbers
from notify.tests import PDF_STORAGE_LINK, import_sample_dfs

secrets_to_environment("notify")


def test_send_single_email():
    message = "This is a test from notify"
    response = NotifyMail(
        to=f"{os.environ.get('TEST_EMAIL_1')}", subject="Test Notify single email", message=message
    ).send_email()
    assert response
    time.sleep(2)


def test_send_email_with_table():
    message = "This is a test from notify"
    df = import_sample_dfs().get("Transactions")

    response = NotifyMail(
        to=f"{os.environ.get('TEST_EMAIL_1')}",
        subject="Test Notify with HTML table",
        message=message,
        df=df,
    ).send_email()
    assert response
    time.sleep(2)


def test_send_email_with_formatted_table():
    message = "This is a test from notify"
    df = import_sample_dfs().get("Transactions")
    df = format_numbers(df, currency_columns=["amount"])
    response = NotifyMail(
        to=f"{os.environ.get('TEST_EMAIL_1')}",
        subject="Test Notify with HTML table with formatted columns",
        message=message,
        df=df,
    ).send_email()
    assert response
    time.sleep(2)


@pytest.mark.parametrize("sep", [",", ";"])
def test_send_multiple_emails(sep: str):
    message = "This is a test from notify"
    to = sep.join(
        [
            os.environ.get("TEST_EMAIL_1"),
            os.environ.get("TEST_EMAIL_2"),
        ]
    )
    response = NotifyMail(
        to=to,
        subject="Test Notify multiple emails",
        message=message,
    ).send_email()
    assert response
    time.sleep(2)


def test_send_file():
    message = "This is a test from notify"
    subject = "Test Notify file"
    file_name = "2010 car efficiency.csv"
    file_path = os.path.join("notify", "tests", "data", file_name)
    response = NotifyMail(
        to=f"{os.environ.get('TEST_EMAIL_1')}",
        subject=subject,
        message=message,
        files={file_name: file_path},
    ).send_email()
    assert response


def test_send_file_from_storage():
    message = "This is a test from notify"
    subject = "Test Notify file Azure Storage"
    response = NotifyMail(
        to=f"{os.environ.get('TEST_EMAIL_1')}",
        subject=subject,
        message=message,
        files={"testpdf.pdf": PDF_STORAGE_LINK},
    ).send_email()
    assert response


def test_send_cc():
    message = "This is a test from notify"
    response = NotifyMail(
        to=f"{os.environ.get('TEST_EMAIL_1')}",
        cc=f"{os.environ.get('TEST_EMAIL_2')}",
        subject="Test Notify cc emails",
        message=message,
    ).send_email()
    assert response
    time.sleep(2)


def test_send_bcc():
    message = "This is a test from notify"
    response = NotifyMail(
        to=f"{os.environ.get('TEST_EMAIL_1')}",
        bcc=f"{os.environ.get('TEST_EMAIL_2')}",
        subject="Test Notify bcc emails",
        message=message,
    ).send_email()
    assert response
    time.sleep(2)


def test_wrong_user():
    mail = NotifyMail(to=os.environ.get("TEST_EMAIL_1"), subject="Test wrong sender", message="Test")
    mail.sender = "wrong@zypp.io"
    with pytest.raises(ODataError):
        mail.send_email()
