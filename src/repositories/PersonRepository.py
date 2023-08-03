from src.database import Database
import psycopg2.extras

class PersonRepository:
    def __init__(self):
        pass

    def create_person(self, person_dto):
        connection = Database.get_connection()
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute('INSERT INTO persons (name, age) VALUES (%s, %s)',
                       (person_dto.name, person_dto.age))
        connection.commit()
        Database.return_connection(connection)

    def get_person(self, person_id):
        connection = Database.get_connection()
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute('SELECT * FROM persons WHERE id = %s', (person_id,))
        person = cursor.fetchone()
        Database.return_connection(connection)
        return person

    def update_person(self, person_id, person_dto):
        connection = Database.get_connection()
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute('UPDATE persons SET name = %s, age = %s WHERE id = %s',
                       (person_dto.name, person_dto.age, person_id))
        connection.commit()
        Database.return_connection(connection)

    def delete_person(self, person_id):
        connection = Database.get_connection()
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute('DELETE FROM persons WHERE id = %s', (person_id,))
        connection.commit()
        Database.return_connection(connection)
