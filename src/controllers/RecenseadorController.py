from src.services.RecenseadorService import recenseadoreservice
from src.dtos.RecenseadorDto import RecenseadorDto

class RecenseadorController:
    def __init__(self):
        self.recenseador_service = recenseadoreservice()

    def create_recenseador(self, recenseador_dto: RecenseadorDto):
        return self.recenseador_service.create_recenseador(recenseador_dto)

    def get_recenseador(self, recenseador_id: int):
        return self.recenseador_service.get_recenseador(recenseador_id)

    def update_recenseador(self, recenseador_id: int, recenseador_dto: RecenseadorDto):
        self.recenseador_service.update_recenseador(recenseador_id, recenseador_dto)
        return self.recenseador_service.get_recenseador(recenseador_id)

    def delete_recenseador(self, recenseador_id: int):
        self.recenseador_service.delete_recenseador(recenseador_id)
        return 200

    def list_recenseadores(self):
        return self.recenseador_service.list_recenseadores()