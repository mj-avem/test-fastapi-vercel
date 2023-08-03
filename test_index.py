import pytest

from src.dtos.ISayHelloDto import ISayHelloDto
from src.repositories.RecenseadorRepository import RecenseadorRepository


# Update the tests to call the methods on an instance of RecenseadorRepository
# Replace the method names and arguments with the actual methods and arguments of the RecenseadorRepository class
@pytest.mark.asyncio
async def test_method1():
    repo = RecenseadorRepository()
    result = await repo.method1()
    assert result == expected_result1

@pytest.mark.asyncio
async def test_method2():
    repo = RecenseadorRepository()
    result = await repo.method2()
    assert result == expected_result2

@pytest.mark.asyncio
async def test_method3():
    repo = RecenseadorRepository()
    result = await repo.method3()
    assert result == expected_result3
    assert result == {'message': 'Hello Alice'}
