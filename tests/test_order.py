import pytest 
from source.order import calculate_order_total as order

def test_invalid_input():
    with pytest.raises(ValueError):
        order([],11)
    with pytest.raises(TypeError):
        order(('abc',), 11)
    with pytest.raises(TypeError):
        order({'key':'str'}, 11)
    with pytest.raises(TypeError):
        order([('abc',)], 11)
    with pytest.raises(ValueError):
        order([{"name":"Shreyash",}], 11)
    with pytest.raises(ValueError):
        order([{"name":11,}], 11)
    with pytest.raises(ValueError):
        order([{"name":  11  ,}], 11)
    with pytest.raises(TypeError):
        order([{"name":"Shreyash" , "price" : "11" , "quantity" : 11}], 11)
    with pytest.raises(ValueError):
        order([{"name":"Shreyash" , "price" : 0 , "quantity" : 11}], 11)
    with pytest.raises(ValueError):
        order([{"name":"Shreyash" , "price" : -1 , "quantity" : 11}], 11)
    with pytest.raises(TypeError):
        order([{"name":"Shreyash" , "price" : 11 , "quantity" : '11'}], 11)
    with pytest.raises(TypeError):
        order([{"name":"Shreyash" , "price" : "11" , "quantity" : -1}], 11)
    with pytest.raises(TypeError):
        order([{"name":"Shreyash" , "price" : "11" , "quantity" : 0}], 11)













    


        #  pytest tests/test_order.py