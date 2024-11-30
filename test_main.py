import pytest
from main import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(3, 5) == 8

def test_restar():
    assert restar(10, 4) == 6

def test_multiplicar():
    assert multiplicar(6, 7) == 42

def test_dividir():
    assert dividir(8, 2) == 4

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(8, 0)
