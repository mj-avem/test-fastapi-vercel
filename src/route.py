from fastapi import APIRouter
from src.controllers.PersonController import PersonController
from src.dtos.PersonDto import PersonDto

router = APIRouter()
person_controller = PersonController()

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
