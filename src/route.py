from fastapi import APIRouter
from src.controllers.PersonController import PersonController
from src.controllers.RecenseadorController import RecenseadorController
from src.dtos.PersonDto import PersonDto
from src.dtos.RecenseadorDto import RecenseadorDto

router = APIRouter()
person_controller = PersonController()
recenseador_controller = RecenseadorController()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.post("/person")
async def create_person(person_dto: PersonDto):
    return person_controller.create_person(person_dto)

@router.get("/person/{person_id}")
async def get_person(person_id: int):
    return person_controller.get_person(person_id)

@router.put("/person/{person_id}")
async def update_person(person_id: int, person_dto: PersonDto):
    return person_controller.update_person(person_id, person_dto)

@router.delete("/person/{person_id}")
async def delete_person(person_id: int):
    return person_controller.delete_person(person_id)

@router.post("/recenseador")
async def create_recenseador(recenseador_dto: RecenseadorDto):
    return recenseador_controller.create_recenseador(recenseador_dto)

@router.get("/recenseador/{recenseador_id}")
async def get_recenseador(recenseador_id: int):
    return recenseador_controller.get_recenseador(recenseador_id)

@router.put("/recenseador/{recenseador_id}")
async def update_recenseador(recenseador_id: int, recenseador_dto: RecenseadorDto):
    return recenseador_controller.update_recenseador(recenseador_id, recenseador_dto)

@router.delete("/recenseador/{recenseador_id}")
async def delete_recenseador(recenseador_id: int):
    return recenseador_controller.delete_recenseador(recenseador_id)
