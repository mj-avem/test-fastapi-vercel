import pytest

from src.dtos.ISayHelloDto import ISayHelloDto
from src.repositories.RecenseadorRepository import RecenseadorRepository


# Update the tests to call the methods on an instance of RecenseadorRepository
# Replace the method names and arguments with the actual methods and arguments of the RecenseadorRepository class
@pytest.mark.asyncio
async def test_create_recenseador():
    repo = RecenseadorRepository()
    recenseador_dto = # Create a RecenseadorDto object with the data for the new recenseador
    repo.create_recenseador(recenseador_dto)
    # Add assertions to check that the recenseador was created correctly

@pytest.mark.asyncio
async def test_get_recenseador():
    repo = RecenseadorRepository()
    recenseador_id = # The ID of the recenseador to get
    recenseador = repo.get_recenseador(recenseador_id)
    # Add assertions to check that the returned recenseador is correct

@pytest.mark.asyncio
async def test_update_recenseador():
    repo = RecenseadorRepository()
    recenseador_id = # The ID of the recenseador to update
    recenseador_dto = # Create a RecenseadorDto object with the new data for the recenseador
    repo.update_recenseador(recenseador_id, recenseador_dto)
    # Add assertions to check that the recenseador was updated correctly

@pytest.mark.asyncio
async def test_delete_recenseador():
    repo = RecenseadorRepository()
    recenseador_id = # The ID of the recenseador to delete
    repo.delete_recenseador(recenseador_id)
    # Add assertions to check that the recenseador was deleted correctly

@pytest.mark.asyncio
async def test_list_recenseadores():
    repo = RecenseadorRepository()
    recenseadores = repo.list_recenseadores()
    # Add assertions to check that the list of recenseadores is correct
