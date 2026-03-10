from tkinter import messagebox
import DAO.GarantiaDAO as garantia_dao

class LogicaGarantia:
    def __init__(self):
        self.garantia_dao = garantia_dao.GarantiaDAO()

    def agregar_garantia(self, modelo_garantia, cursor):
        return self.garantia_dao.agregar_garantia(modelo_garantia, cursor)
    
    def obtener_garantia_por_id(self, id_garantia, cursor):
        return self.garantia_dao.obtener_garantia_por_id(id_garantia, cursor)

    def actualizar_garantia(self, modelo_garantia, cursor):
        return self.garantia_dao.actualizar_garantia(modelo_garantia, cursor)