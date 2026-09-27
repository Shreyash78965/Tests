import pytest
from source.bank import BankAccount

def test_init():
    BankAccount()
    with pytest.raises(TypeError):
        BankAccount('abc')
    with pytest.raises(ValueError):
        BankAccount(-1)
    
def test_deposit():
    account =  BankAccount()
    with pytest.raises(TypeError):
        account.deposit('abc')
    with pytest.raises(ValueError):
        account.deposit(-1)

def test_result_deposit():
    account =  BankAccount(100)
    
    total = account.deposit(100)
    assert total == 200

def test_withdraw():
    account =  BankAccount()
    with pytest.raises(TypeError):
        account.withdraw('abc')
    with pytest.raises(ValueError):
        account.withdraw(-1)
    BankAccount(20)
    with pytest.raises(ValueError):
        account.withdraw(111)

def test_result_withdraw():
    account =  BankAccount(20)
    draw = account.withdraw(10)
    assert draw == 10

def test_deposit_withdraw():
    account = BankAccount(100)
    account.deposit(100)
    total = account.withdraw(100)
    assert total == 100

