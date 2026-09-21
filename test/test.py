from src.main import *
from unittest.mock import patch


def test_root():
    assert root() == {"message": "Fala meu povo"}


def test_funcaoteste():
    return funcaoteste() == {"glauglau": "esteéomain"}


def test_create_estudante():
    estudante_teste = Estudante(name="Lucas", curso="ADS", ativo=True)
    assert estudante_teste == create_estudante()


def test_update_estudante_negativo():
    assert not update_estudante(-5)


def test_update_estudante_positivo():
    assert update_estudante(10)


def test_delete_estudante_negativo():
    assert not delete_estudante(-5)


def test_delete_estudante_positivo():
    assert not delete_estudante(10)
