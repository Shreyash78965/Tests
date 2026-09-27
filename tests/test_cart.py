import pytest
from source.shoppingcart import ShoppingCart

def test_price():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item('toy', 0.0)
def test_discount():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.get_total(-1)
    with pytest.raises(ValueError):
        cart.get_total(111)
def test_total():
    cart = ShoppingCart()
    result = cart.get_total(10)
    assert result == pytest.approx(result)
def test_invalid_inputs():
    cart = ShoppingCart()
    with pytest.raises(TypeError):
        cart.add_item(11,'abc')
    with pytest.raises(TypeError):
        cart.add_item('abc', 'abc')
    with pytest.raises(TypeError):
        cart.get_total('abc')
                      