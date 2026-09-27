import pytest
from source.grade import calculate_grade

def test_input():
    with pytest.raises(TypeError):
        calculate_grade('abc')
    
    with pytest.raises(ValueError):
        calculate_grade(-1)

    with pytest.raises(ValueError):
        calculate_grade(111)

def test_A():
    result = calculate_grade(95)
    assert result == 'A'

def test_B():
    result = calculate_grade(85)
    assert result == 'B'

def test_C():
    result = calculate_grade(70)
    assert result == 'C'

def test_D():
    result = calculate_grade(45)
    assert result == 'D'

def test_F():
    result = calculate_grade(30)
    assert result == 'F'
    