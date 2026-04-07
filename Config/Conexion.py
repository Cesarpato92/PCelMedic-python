import os
from dotenv import load_dotenv

import mysql.connector
from mysql.connector import Error


class Conexion:
    load_dotenv()  # Carga las variables de .env al entorno
    __conexion = None
    # atributos de conexión 
    __port = os.getenv("DB_PORT", "3306")
    __host = os.getenv("DB_HOST", "localhost")
    __user = os.getenv("DB_USER", "root")
    __password = os.getenv("DB_PASSWORD", "1234")
    __database = os.getenv("DB_DATABASE", "pcelmedic")

    # ... __init__ vacío ...

    @classmethod
    def get_conexion(cls):
        
        if cls.__conexion is None or not cls.__conexion.is_connected():
            try:
                cls.__conexion = mysql.connector.connect(
                    host=cls.__host, 
                    port=cls.__port, 
                    user=cls.__user, 
                    password=cls.__password, 
                    database=cls.__database)
                if cls.__conexion.is_connected():
                    print("Conexión exitosa a la base de datos.")
            except Error as err:
                print(f"Error al conectar a la base de datos: {err}")
                return None
        return cls.__conexion

    @classmethod
    def desconectar(cls):
        if cls.__conexion is not None and cls.__conexion.is_connected():
            cls.__conexion.close()
            cls.__conexion = None
            print("Conexión a la base de datos cerrada.")
