from src.math_operation import add , sub

def test_add():
    assert add(2 , 3) == 5
    assert add(8 , 3) == 11

    assert add(1 , 4) == 5

    
    
def test_sub()   :
    assert sub(2 , 1) == 1
    
    