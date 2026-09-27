import pytest
from source.factorial import factorial 

def test_input():
    with pytest.raises(TypeError):
        factorial('abc')
    with pytest.raises(TypeError):
        factorial(11.3)
    with pytest.raises(ValueError):
        factorial(-1)

def test_result():
    result = factorial(4)
    assert result == 24