import pytest
from source.email import is_valid_email

def test_email_dot():
   mail = "shreyashgholasgaon@gmail..com"
   number = mail.count(".")
   if number > 2:
       assert is_valid_email("shreyashgholasgaon@gmail..com") is False
def test_at_the_rate():
    mail = "shreyashgholasgaon@@gmail.com"
    number = mail.count("@")
    if number > 2:
        assert is_valid_email("shreyashgholasgaon@@gmail.com") is False
def test_attherate_first():
    assert is_valid_email("@shreyashgholasgaongmail.com") is False
def test_attherate_last():
    assert is_valid_email("shreyashgholasgaongmail.com@") is False
def test_dot_first():
    assert is_valid_email(".shreyashgholasgaon@gmailcom") is False
def test_dot_last():
    assert is_valid_email("shreyashgholasgaon@gmailcom.") is False
def test_invalid_inputs():
    assert is_valid_email('123') is False
    assert is_valid_email("shreyashgholasgaon") is False
def test_valid_email():
    assert is_valid_email("shreyashgholasgaon@gmail.com") is True