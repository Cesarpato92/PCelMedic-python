from tkinter import messagebox
import DAO.DispositivoDAO as dispositivo_dao

class LogicaDispositivo:
    #Inyectamos las dependencias dentro del constructor
    def __init__(self):
        self.dispositivo_dao = dispositivo_dao.DispositivoDAO()
        
    """En los metodos de la logica simplemente llamamos a los metodos del DAO correspondiente
    en cada metodo realizamos las validaciones o reglas de negocio necesarias antes o despues de llamar al DAO
    Verificamos que los datos sean correctos antes de llamar al DAO, etc."""
    def agregar_dispositivo(self, modelo_dispositivo):
        
        if self.validacion_datos(modelo_dispositivo):
            # Llamamos al DAO para agregar el dispositivo luego de pasar las validaciones
            return self.dispositivo_dao.agregar_dispositivo(modelo_dispositivo)

    def obtener_dispositivo_por_id(self, id_disp):
        return self.dispositivo_dao.obtener_dispositivo_por_id(id_disp)
    
    def actualizar_dispositivo(self, modelo_dispositivo):
        self.dispositivo_dao.actualizar_dispositivo(modelo_dispositivo)
    
    def validacion_datos(self, modelo_dispositivo):
        # Validaciones básicas
        if not modelo_dispositivo.marca or modelo_dispositivo.marca.strip() == "":
            messagebox.showerror("Error", "La marca es obligatoria.")
            return False
        
        if not modelo_dispositivo.tipo_reparacion or modelo_dispositivo.tipo_reparacion.strip() == "":
            messagebox.showerror("Error", "El tipo de reparación es obligatorio.")
            return False
        
        if len(modelo_dispositivo.marca) > 45:
            messagebox.showerror("Error", "No superar los 45 caracteres.")
            return False
        
        if modelo_dispositivo.tipo_password in ["PIN", "Contraseña", "Patrón"]:
            if not modelo_dispositivo.password or modelo_dispositivo.password.strip() == "":
                messagebox.showerror("Error", f"La contraseña para el tipo {modelo_dispositivo.tipo_password} es obligatoria.")
                return False
            
        if len(modelo_dispositivo.password) > 40:
            messagebox.showerror("Error", "No superar los 40 caracteres.")
            return False
        
        if not modelo_dispositivo.comentarios or modelo_dispositivo.comentarios.strip() == "":
            messagebox.showerror("Error", "Debe dejar comentarios para la reparacion.")
            return False
        
        return True