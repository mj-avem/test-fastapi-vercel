import os
from psycopg2 import pool

class Database:
    __connection_pool = None

    @staticmethod
    def initialise():
        Database.__connection_pool = pool.SimpleConnectionPool(
            1, 
            10,
            host=os.getenv('DATABASE_HOST'),
            port=os.getenv('DATABASE_PORT'),
            dbname=os.getenv('DATABASE_NAME'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD')
        )

    @staticmethod
    def get_connection():
        if Database.__connection_pool is None:
            Database.initialise()
        return Database.__connection_pool.getconn()

    @staticmethod
    def return_connection(connection):
        Database.__connection_pool.putconn(connection)

    @staticmethod
    def close_all_connections():
        Database.__connection_pool.closeall()
