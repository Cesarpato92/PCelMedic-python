from tkinter import messagebox
import DAO.ReparacionDAO as reparacion_dao

class LogicaReparacion:
    def __init__(self):
        self.reparacion_dao = reparacion_dao.ReparacionDAO()

    def agregar_reparacion(self, modelo_reparacion, cursor):
        if self.validacion_datos_para_agregar(modelo_reparacion, cursor):
            return self.reparacion_dao.agregar_reparacion(modelo_reparacion, cursor)

    def actualizar_estado_reparacion(self, modelo_reparacion, cursor):
        if self.validacion_datos_cambiar_estado(modelo_reparacion):
            return self.reparacion_dao.actualizar_estado_reparacion(modelo_reparacion, cursor)

    def obtener_reparacion_por_id(self, id_reparacion, cursor):
        if self.validacion_id_reparacion(id_reparacion):
            return self.reparacion_dao.obtener_reparacion_por_id(id_reparacion, cursor)

   
    
    def validacion_datos_para_agregar(self, modelo_reparacion):
        if modelo_reparacion.costo_repuestos is None or modelo_reparacion.costo_repuestos <= 0:
            messagebox.showerror("Error", "El costo del repuesto debe ser mayor a 0.")
            return False
        
        if modelo_reparacion.comentarios is None or modelo_reparacion.comentarios == "":
            messagebox.showerror("Error", "El comentario es obligatorio.")
            return False
        
        if modelo_reparacion.repuesto is None or modelo_reparacion.repuesto == "":
            messagebox.showerror("Error", "El repuesto es obligatorio.")
            return False
        return True

    def validacion_datos_cambiar_estado(self, modelo_reparacion):
        # validar números correctamente
        if modelo_reparacion.costo_repuestos is not None and modelo_reparacion.costo_repuestos < 0:
            messagebox.showerror("Error", "El costo del repuesto no puede ser negativo.")
            return False
            
        if modelo_reparacion.estado not in ["En Proceso", "Completada", "Entregada"]:
            messagebox.showerror("Error", "El estado de la reparación no es válido.")
            return False
        
        if modelo_reparacion.comentarios is None or modelo_reparacion.comentarios == "":
            messagebox.showerror("Error", "El comentario es obligatorio.")
            return False
        return True

    def validacion_id_reparacion(self, id_reparacion):
        if not id_reparacion.isdigit():
            messagebox.showerror("Error", "El ID de la reparación debe ser un número.")
            return False
        if int(id_reparacion) <=0:
            messagebox.showerror("Error", "El ID de la reparación no puede ser negativo.")
            return False
        if int(id_reparacion) > 2147483647:
            messagebox.showerror("Error", "El ID de la reparación no puede superar los 2147483647.")
            return False
        return True