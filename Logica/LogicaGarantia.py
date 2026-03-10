from tkinter import messagebox
import DAO.GarantiaDAO as garantia_dao

class LogicaGarantia:
    def __init__(self):
        self.garantia_dao = garantia_dao.GarantiaDAO()

    def agregar_garantia(self, modelo_garantia, cursor):
        if self.validar_campos(modelo_garantia):
            return self.garantia_dao.agregar_garantia(modelo_garantia, cursor)
    
    def obtener_garantia_por_id(self, id_garantia, cursor):
        if self.validar_id(id_garantia):
            return self.garantia_dao.obtener_garantia_por_id(id_garantia, cursor)

    def actualizar_garantia(self, modelo_garantia, cursor):
        if self.validar_campos(modelo_garantia):
            return self.garantia_dao.actualizar_garantia(modelo_garantia, cursor)
    
    def validar_id(self, id_garantia):
        if not id_garantia or id_garantia.strip() == "":
            messagebox.showerror("Error", "el id de garantia no puede estar vacía.")
            return False
        if not id_garantia.isdigit():
            messagebox.showerror("Error", "El id solo debe de contener numeros.")
            return False
        if len(id_garantia.strip()) < 0:
            messagebox.showerror("Error", "El id debe ser un numero mayor a cero (0)")
            return False
        # Validacion de INT que no supere el valor maximo
        if id_garantia.strip() > 4294967295:
            messagebox.showerror("Error", "valor muy largo.")
            return False
        return True
    
    def validar_campos(self, modelo_garantia):
        pass