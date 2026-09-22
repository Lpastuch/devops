import pytest

from src.main import *
from unittest.mock import patch


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Fala meu povo"}


@pytest.mark.asyncio
async def test_funcaoteste():
    result = await funcaoteste()
    return result == {"glauglau": "esteéomain"}


@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Lucas", curso="ADS", ativo=True)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result


@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result


@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result


@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result


@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(10)
    assert not result
