from src.repositories.PersonRepository import PersonRepository

class PersonService:
    def __init__(self):
        self.person_repository = PersonRepository()

    def create_person(self, person_dto):
        return self.person_repository.create_person(person_dto)

    def get_person(self, person_id):
        return self.person_repository.get_person(person_id)

    def update_person(self, person_id, person_dto):
        return self.person_repository.update_person(person_id, person_dto)

    def delete_person(self, person_id):
        return self.person_repository.delete_person(person_id)
