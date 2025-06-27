from seasons import get_date, convert
import pytest, datetime

def test_get_date_text():
    with pytest.raises(ValueError):
        get_date("hello")

def test_get_date_format():
    with pytest.raises(ValueError):
        get_date("January 1st, 2000")

def test_get_date():
        assert get_date("1989-06-28") == datetime.date(1989, 6, 28)

def test_convert():
    assert convert(10477) == "Ten thousand, four hundred seventy-seven"
