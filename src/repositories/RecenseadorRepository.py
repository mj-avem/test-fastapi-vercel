from src.database import Database
import psycopg2.extras
from src.models.RecenseadorModel import RecenseadorModel

class RecenseadorRepository:
    def __init__(self):
        pass

    def create_recenseador(self, recenseador_dto):
        connection = Database.get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO recenseadores (nome, usuario, senha, email, data_nascimento, ativo) VALUES (%s, %s, %s, %s, %s, %s)',
                       (recenseador_dto.nome, recenseador_dto.usuario, recenseador_dto.senha, recenseador_dto.email, recenseador_dto.data_nascimento, recenseador_dto.ativo))
        connection.commit()
        connection.close()

    def get_recenseador(self, recenseador_id):
        connection = Database.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM recenseadores WHERE id = %s', (recenseador_id,))
        recenseador = cursor.fetchone()
        connection.close()
        return recenseador

    def update_recenseador(self, recenseador_id, recenseador_dto):
        connection = Database.get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE recenseadores SET nome = %s, usuario = %s, senha = %s, email = %s, data_nascimento = %s, ativo = %s WHERE id = %s',
                       (recenseador_dto.nome, recenseador_dto.usuario, recenseador_dto.senha, recenseador_dto.email, recenseador_dto.data_nascimento, recenseador_dto.ativo, recenseador_id))
        connection.commit()
        connection.close()

    def delete_recenseador(self, recenseador_id):
        connection = Database.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM recenseadores WHERE id = %s', (recenseador_id,))
        connection.commit()
        connection.close()

    def list_recenseadores(self):
        connection = Database.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM recenseadores')
        recenseadores = cursor.fetchall()
        connection.close()
        return recenseadores
