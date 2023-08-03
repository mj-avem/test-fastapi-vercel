from src.repositories.RecenseadorRepository import RecenseadorRepository
from src.dtos.RecenseadorDto import RecenseadorDto

class RecenseadorService:
    def __init__(self):
        self.recenseador_repository = RecenseadorRepository()

    def create_recenseador(self, recenseador_dto: RecenseadorDto):
        return self.recenseador_repository.create_recenseador(recenseador_dto)

    def get_recenseador(self, recenseador_id: int):
        return self.recenseador_repository.get_recenseador(recenseador_id)

    def update_recenseador(self, recenseador_id: int, recenseador_dto: RecenseadorDto):
        return self.recenseador_repository.update_recenseador(recenseador_id, recenseador_dto)

    def delete_recenseador(self, recenseador_id: int):
        return self.recenseador_repository.delete_recenseador(recenseador_id)
