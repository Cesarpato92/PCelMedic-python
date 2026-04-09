from Config.Conexion import Conexion

class TransaccionConexion:
   
    def __init__(self):
        self.conexion = Conexion.get_conexion()
        self.cursor = None

    def __enter__(self):
        if self.conexion is None:
            raise ConnectionError("No se pudo establecer la conexión a la base de datos.")

        # Verificamos que no haya una conexion en curso
        if not self.conexion.in_transaction:
            self.conexion.start_transaction()
        else:
            # Si ya hay una hacemos rollback para limpiar
            self.conexion.rollback()
            self.conexion.start_transaction()
            
        self.cursor = self.conexion.cursor()
        return self.cursor, self.conexion

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            # Si ocurrió una excepción, hacemos rollback
            self.conexion.rollback()
        
        # si existe cursor cerramos la conexion
        if self.cursor:
            self.cursor.close()

    def commit(self):
        self.conexion.commit()
    
    def rollback(self):
        self.conexion.rollback()