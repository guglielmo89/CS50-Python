from numb3rs import validate

def test_validate_valid():
    assert validate("192.169.0.1") == True

def test_validate_invalid_1():
    assert validate("300.1.1.1") == False

def test_validate_invalid_2():
    assert validate("300") == False

def test_validate_invalid_3():
    assert validate("cat") == False

def test_validate_first_byte():
    assert validate("999.1.1.1") == False
    assert validate("1.999.1.1") == False
    assert validate("1.1.999.1") == False
    assert validate("1.1.1.999") == False
    assert validate("1.1.1.1") == True
