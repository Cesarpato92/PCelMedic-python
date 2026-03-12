from tkinter import messagebox
import DAO.GarantiaDAO as garantia_dao

class LogicaGarantia:
    def __init__(self):
        self.garantia_dao = garantia_dao.GarantiaDAO()

    def agregar_garantia(self, modelo_garantia, cursor):
        if self.validar_campos_a_insertar(modelo_garantia):
            return self.garantia_dao.agregar_garantia(modelo_garantia, cursor)
    
    def obtener_garantia_por_id(self, id_garantia, cursor):
        if self.validar_id(id_garantia):
            return self.garantia_dao.obtener_garantia_por_id(id_garantia, cursor)

    def actualizar_garantia(self, modelo_garantia, cursor):
        if self.validar_campos_a_actualizar(modelo_garantia):
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
    def validar_estado(self, estado):
        estados_validos = ["Completada", "En Proceso", "Rechazada"]
        if estado not in estados_validos:
            messagebox.showerror("Error", "El estado no es válido.")
            return False
        return True

    def validar_observaciones(self, observaciones):
        if observaciones is None or observaciones == "":
            messagebox.showerror("Error", "Las observaciones son obligatorias.")
            return False
        return True

    def validar_fecha_inicio(self, fecha_inicio):
        if fecha_inicio is None or fecha_inicio == "":
            messagebox.showerror("Error", "La fecha de inicio es obligatoria.")
            return False
        return True
    def validar_fecha_fin(self, fecha_fin):
        if fecha_fin is None or fecha_fin == "":
            messagebox.showerror("Error", "La fecha de finalizacion es obligatoria.")
            return False
        return True

    def validar_precio_insumos(self, precio_insumos):
        if precio_insumos is None or precio_insumos == "":
            messagebox.showerror("Error", "El precio de los insumos es obligatorio")
            return False
        if not precio_insumos.strip().isdigit():
            messagebox.showerror("Error", "El precio de insumos solo debe de ser numeros.")
            return False
        return True

    def validar_comentarios_finales(self, comentarios_finales):
        if comentarios_finales is None or comentarios_finales == "":
            messagebox.showerror("Error", "Los comentarios finales de garantia son obligatorios")
            return False
        return True

    def validar_campos_a_insertar(self, modelo_garantia):

        if not self.validar_estado(modelo_garantia.estado):
            return False
        if not self.validar_observaciones(modelo_garantia.observaciones):
            return False
        if not self.validar_fecha_inicio(modelo_garantia.fecha_inicio):
            return False
        return True

    def validar_campos_a_actualizar(self, modelo_garantia):
        
        if not self.validar_estado(modelo_garantia.estado):
            return False
        if not self.validar_fecha_fin(modelo_garantia.fecha_fin):
            return False
        if not self.validar_comentarios_finales(modelo_garantia.comentarios_finales):
            return False
        return True