import pytest
from source.registration import register_user

@pytest.mark.xfail(reason="for now")
def test_if_float():
     register_user('shreyash', 11.2)
@pytest.mark.invalid
def test_invalid_inputs():
    with pytest.raises(TypeError):
        register_user(11,11)
    with pytest.raises(ValueError):
        register_user("",11)
    with pytest.raises(TypeError):
       register_user('shreyash', 'gholasgaon')

@pytest.mark.slow()
def test_underage():
    with pytest.raises(ValueError):
        register_user("shreyash",11)

def test_valid_input():
    assert register_user("shreyash",18) =='User shreyash registered successfully'
    assert register_user("shreyash",20) =='User shreyash registered successfully'
    
# pytest tests/test_registration.py