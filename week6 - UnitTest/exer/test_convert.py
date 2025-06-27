import pytest
from convert import convert

AU = 149597870700

def test_int_conversion():
    assert convert(1) == AU
    assert convert(50) == 50 * AU


def test_error():
    with pytest.raises(TypeError):
        convert("1")

def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691, abs=0.1)
