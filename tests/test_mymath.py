import pytest
import source.mymath as mymath


def test_add():
    result = mymath.add(10,20)
    assert result == 30

def test_substract():
    result = mymath.subtract(10, 20)
    assert result ==-10

def test_multiply():
    result = mymath.multiply(10,20)
    assert result == 200

def test_divide():
    result = mymath.divide(20,10)
    assert result == 2

@pytest.mark.skip(reason='Just skip for now')
def test_ZeroDivisioN():
     mymath.divide(10,0)

# def test_ZeroDivisioN():
#     with pytest.raises(ZeroDivisionError):
#         mymath.divide(10,0)
# pytest tests/test_mymath.py