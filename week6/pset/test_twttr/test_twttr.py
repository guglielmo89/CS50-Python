from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"

def test_shorten_capital():
    assert shorten("twIttEr") == "twttr"

def test_number():
    assert shorten("0") == "0"
    assert shorten("1.5") == "1.5"

def test_punctuation():
    assert shorten("?,.!") == "?,.!"
