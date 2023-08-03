from fastapi import APIRouter
from src.controllers.RecenseadorController import RecenseadorController
from src.dtos.RecenseadorDto import RecenseadorDto

router = APIRouter()
recenseador_controller = RecenseadorController()

@router.get("/")
async def root():
    return {"message": "Ok"}

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

@router.get("/recenseadors")
async def list_recenseadors():
    return recenseador_controller.list_recenseadors()
