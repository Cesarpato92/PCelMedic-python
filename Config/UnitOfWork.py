from Config.Conexion import Conexion
from DAO.ClienteDAO import ClienteDAO
from DAO.DispositivoDAO import DispositivoDAO
from DAO.ReparacionDAO import ReparacionDAO
from DAO.GarantiaDAO import GarantiaDAO
from DAO.FacturasDAO import FacturasDAO

class UnitOfWork:
    def __init__(self):
        self.conexion = Conexion.get_conexion()
        self.cursor = None
        # DAOs
        self.clientes = ClienteDAO()
        self.dispositivos = DispositivoDAO()
        self.reparaciones = ReparacionDAO()
        self.garantias = GarantiaDAO()
        self.facturas = FacturasDAO()

    def __enter__(self):
        if self.conexion is None:
            raise ConnectionError("No se pudo establecer la conexión a la base de datos.")
            
        if not self.conexion.in_transaction:
            self.conexion.start_transaction()
            
        self.cursor = self.conexion.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()
        if self.cursor:
            self.cursor.close()

    def commit(self):
        if self.conexion:
            self.conexion.commit()

    def rollback(self):
        if self.conexion:
            self.conexion.rollback()
