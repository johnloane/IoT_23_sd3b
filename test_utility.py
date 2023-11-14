from utility import square
from utility import hello
import pytest


def test_positive_square():
    assert square(2) == 4
    assert square(3) == 9


def test_negative_square():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero_square():
    assert square(0) == 0


def test_string_square():
    with pytest.raises(TypeError):
        square('ciaran')


def test_none_square():
    with pytest.raises(TypeError):
        square(None)


def test_float_square():
    with pytest.raises(TypeError):
        square(2.5)


def test_default_hello():
    assert hello() == "Hello World!"


def test_argument_hello():
    assert hello("Ciaran") == "Hello Ciaran!"


def test_none_hello():
    assert hello(None) == "Hello None!"


def test_empty_hello():
    assert hello("") == "Hello !"



  
    
