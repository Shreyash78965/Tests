import pytest
from source.library import Book  
from source.library import Library

@pytest.fixture
def bo():
    return Book('Beyond Good And Evil' , 'Nietzsche')

@pytest.fixture
def lib():
    return lib(bo)
def test_add_book():
    with pytest.raises(ValueError):
        lib
        
