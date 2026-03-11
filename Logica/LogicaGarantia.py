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
            messagebox.showerror("Error", "El id de garantía no puede estar vacío.")
            return False
            
        if not id_garantia.strip().isdigit():
            messagebox.showerror("Error", "El id solo debe contener números.")
            return False
            
        # Convertir a entero para comparaciones numéricas
        try:
            id_num = int(id_garantia.strip())
        except ValueError:
            messagebox.showerror("Error", "El id debe ser un número válido.")
            return False
            
        if id_num <= 0:
            messagebox.showerror("Error", "El id debe ser un número mayor a cero.")
            return False
            
        # comparar entero con entero
        MAX_ID = 4294967295
        if id_num > MAX_ID:
            messagebox.showerror("Error", f"El id no puede ser mayor a {MAX_ID}.")
            return False
            
        return True
    
    def validar_campos(self, modelo_garantia):
        # TODO: Implementar validación de campos del modelo
        return True