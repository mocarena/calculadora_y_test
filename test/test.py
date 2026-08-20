import pytest

from calculadora import sumar, restar, multiplicar, dividir


# Fixture con valores enteros
@pytest.fixture
def enteros():
    return 10, 5


# Fixture con valores flotantes
@pytest.fixture
def flotantes():
    return 0.1, 0.2


# =========================
# SUMAR
# =========================

@pytest.mark.smoke
@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (5, 5, 10),
        (10, 20, 30),
        (-5, 10, 5)
    ]
)
def test_sumar(a, b, esperado):
    assert sumar(a, b) == esperado


@pytest.mark.smoke
def test_sumar_con_enteros(enteros):
    a, b = enteros
    assert sumar(a, b) == 15


# =========================
# RESTAR
# =========================

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (10, 5, 5),
        (20, 10, 10),
        (5, 10, -5)
    ]
)
def test_restar(a, b, esperado):
    assert restar(a, b) == esperado


def test_restar_con_enteros(enteros):
    a, b = enteros
    assert restar(a, b) == 5


# =========================
# MULTIPLICAR
# =========================

def test_multiplicar_con_enteros(enteros):
    a, b = enteros
    assert multiplicar(a, b) == 50


def test_multiplicar_con_flotantes(flotantes):
    a, b = flotantes
    assert multiplicar(a, b) == pytest.approx(0.02)


# =========================
# DIVIDIR
# =========================

def test_dividir_con_enteros(enteros):
    a, b = enteros
    assert dividir(a, b) == 2


def test_dividir_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        dividir(10, 0)


@pytest.mark.exception
def test_dividir_por_cero_exception():
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        dividir(10, 0)