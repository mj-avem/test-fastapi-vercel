from src.services.RecenseadorService import RecenseadorService
from src.dtos.RecenseadorDto import RecenseadorDto

class RecenseadorController:
    def __init__(self):
        self.recenseador_service = RecenseadorService()

    def create_recenseador(self, recenseador_dto: RecenseadorDto):
        return self.recenseador_service.create_recenseador(recenseador_dto)

    def get_recenseador(self, recenseador_id: int):
        return self.recenseador_service.get_recenseador(recenseador_id)

    def update_recenseador(self, recenseador_id: int, recenseador_dto: RecenseadorDto):
        return self.recenseador_service.update_recenseador(recenseador_id, recenseador_dto)

    def delete_recenseador(self, recenseador_id: int):
        return self.recenseador_service.delete_recenseador(recenseador_id)
