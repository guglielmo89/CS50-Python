from bank import value

def test_value_hello():
    assert value("hello") == 0

def test_value_hello_upper():
    assert value("Hello") == 0

def test_value_hi():
    assert value("hi") == 20

def test_value_else():
    assert value("ciao") == 100
