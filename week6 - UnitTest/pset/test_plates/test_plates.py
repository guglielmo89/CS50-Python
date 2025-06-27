from plates import is_valid


def test_valid_1():
    assert is_valid("50") == False

def test_valid_2():
    assert is_valid("CS50") == True

def test_valid_3():
    assert is_valid("CS05") == False

def test_valid_4():
    assert is_valid("CS50P") == False

def test_valid_5():
    assert is_valid("PI3.14") == False

def test_valid_6():
    assert is_valid("H") == False

def test_valid_7():
    assert is_valid("OUTATIME") == False
