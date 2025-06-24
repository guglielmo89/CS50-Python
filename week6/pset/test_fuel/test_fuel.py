from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_convert_greater():
    with pytest.raises(ValueError):
        convert("5/4")

def test_convert_string_X():
    with pytest.raises(ValueError):
        convert("cat/4")

def test_convert_string_Y():
    with pytest.raises(ValueError):
        convert("4/cat")

def test_convert_string_XY():
    with pytest.raises(ValueError):
        convert("dog/cat")

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
