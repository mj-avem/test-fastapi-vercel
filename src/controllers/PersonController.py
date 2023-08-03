from flask import request
from src.services.PersonService import PersonService
from src.dtos.PersonDto import PersonDto

class PersonController:
    def __init__(self):
        self.person_service = PersonService()

    def create_person(self):
        person_dto = PersonDto(**request.json)
        return self.person_service.create_person(person_dto)

    def get_person(self, person_id):
        return self.person_service.get_person(person_id)

    def update_person(self, person_id):
        person_dto = PersonDto(**request.json)
        return self.person_service.update_person(person_id, person_dto)

    def delete_person(self, person_id):
        return self.person_service.delete_person(person_id)
