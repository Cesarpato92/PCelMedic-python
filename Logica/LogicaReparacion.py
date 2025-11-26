from tkinter import messagebox
import DAO.ReparacionDAO as reparacion_dao

class LogicaReparacion:
    def __init__(self):
        self.reparacion_dao = reparacion_dao.ReparacionDAO()

    def agregar_reparacion(self, modelo_reparacion):
        if self.validacion_datos_para_agregar(modelo_reparacion):
            return self.reparacion_dao.agregar_reparacion(modelo_reparacion)

    def actualizar_estado_reparacion(self, modelo_reparacion):
        if modelo_reparacion.estado not in ["En Proceso", "Completada", "Entregada"]:
            messagebox.showerror("Error", "El estado de la reparación no es válido.")
            return
        self.reparacion_dao.actualizar_estado_reparacion(modelo_reparacion)

    def obtener_reparacion_por_id(self, modelo_reparacion):
        # eliminar la validación incorrecta
        return self.reparacion_dao.obtener_reparacion_por_id(modelo_reparacion)
    
    def validacion_datos_para_agregar(self, modelo_reparacion):
        # Validaciones básicas
        # validar números correctamente
        if modelo_reparacion.precio_reparacion is None or modelo_reparacion.precio_reparacion <= 0:
            messagebox.showerror("Error", "El precio de reparación debe ser mayor a 0.")
            return False
        return True

    def validacion_datos_cambiar_estado(self, modelo_reparacion):
        if not modelo_reparacion.fecha_ingreso:
            messagebox.showerror("Error", "La fecha de ingreso es obligatoria.")
            return False
            
        # validar números correctamente
        if modelo_reparacion.costo_repuestos is not None and modelo_reparacion.costo_repuestos < 0:
            messagebox.showerror("Error", "El costo del repuesto no puede ser negativo.")
            return False
            
        if modelo_reparacion.estado not in ["En Proceso", "Completada", "Entregada"]:
            messagebox.showerror("Error", "El estado de la reparación no es válido.")
            return False
            
        # validar números correctamente  
        if modelo_reparacion.precio_reparacion is not None and modelo_reparacion.precio_reparacion < 0:
            messagebox.showerror("Error", "El precio de la reparación no puede ser negativo.")
            return False
            
        return True