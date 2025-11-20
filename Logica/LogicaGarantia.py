from tkinter import messagebox
import DAO.GarantiaDAO as garantia_dao

class LogicaGarantia:
    def __init__(self):
        self.garantia_dao = garantia_dao.GarantiaDAO()

    def agregar_garantia(self, modelo_garantia):
        return self.garantia_dao.agregar_garantia(modelo_garantia)
    
    def obtener_garantia_por_id(self, id_garantia):
        return self.garantia_dao.obtener_garantia_por_id(id_garantia)