from tkinter import messagebox
import DAO.DispositivoDAO as dispositivo_dao

class LogicaDispositivo:
    #Inyectamos las dependencias dentro del constructor
    def __init__(self):
        self.dispositivo_dao = dispositivo_dao.DispositivoDAO()
        
    """En los metodos de la logica simplemente llamamos a los metodos del DAO correspondiente
    en cada metodo realizamos las validaciones o reglas de negocio necesarias antes o despues de llamar al DAO
    Verificamos que los datos sean correctos antes de llamar al DAO, etc."""
    def agregar_dispositivo(self, modelo_dispositivo, cursor):
        
        if self.validacion_datos(modelo_dispositivo):
            # Llamamos al DAO para agregar el dispositivo luego de pasar las validaciones
            return self.dispositivo_dao.agregar_dispositivo(modelo_dispositivo, cursor)

    def obtener_dispositivo_por_id(self, id_disp, cursor):
        if self.validacion_id_dispositivo(id_disp):
            return self.dispositivo_dao.obtener_dispositivo_por_id(id_disp, cursor)
    
    def actualizar_dispositivo(self, modelo_dispositivo, cursor):
        self.dispositivo_dao.actualizar_dispositivo(modelo_dispositivo, cursor)
    
    def validacion_datos(self, modelo_dispositivo):
        # Validaciones básicas

        if not self.validacion_marca(modelo_dispositivo.marca):
            return False
        if not self.validacion_tipo_reparacion(modelo_dispositivo.tipo_reparacion):
            return False
        if not self.validacion_tipo_password(modelo_dispositivo.tipo_password):
            return False
        if not self.validacion_password(modelo_dispositivo.password, modelo_dispositivo.tipo_password):
            return False
        if not self.validacion_comentarios(modelo_dispositivo.comentarios):
            return False
        if not self.validacion_version(modelo_dispositivo.version):
            return False
        return True
    
    def validacion_id_dispositivo(self, id_disp):
              
        if not id_disp.isdigit():
            messagebox.showerror("Error", "El ID del dispositivo debe ser un número.")
            return False
        if int(id_disp) <=0:
            messagebox.showerror("Error", "El ID del dispositivo no puede ser negativo.")
            return False
        if int(id_disp) > 2147483647:
            messagebox.showerror("Error", "El ID del dispositivo no puede superar los 2147483647.")
            return False
        return True

    def validacion_marca(self, marca):
        if not marca or marca.strip() == "":
            messagebox.showerror("Error", "La marca es obligatoria.")
            return False
        if len(marca) > 45:
            messagebox.showerror("Error", "La marca no puede superar los 45 caracteres.")
            return False
        return True

    def validacion_tipo_reparacion(self, tipo_reparacion):
        opciones_rep = ["Display", "Puerto de carga", "Corto", "Sonido", "Cuenta", "Bloqueo", "Otro"]
        if not tipo_reparacion or tipo_reparacion.strip() == "":
            messagebox.showerror("Error", "El tipo de reparación es obligatorio.")
            return False
        if tipo_reparacion not in opciones_rep:
            messagebox.showerror("Error", "El tipo de reparación no es válido.")
            return False
        if len(tipo_reparacion) > 100:
            messagebox.showerror("Error", "El tipo de reparación no puede superar los 100 caracteres.")
            return False
        return True
    def validacion_tipo_password(self, tipo_password):
        opciones_pass = ["PIN", "Contraseña", "Patrón"]
        if not tipo_password or tipo_password.strip() == "":
            messagebox.showerror("Error", "El tipo de contraseña es obligatorio.")
            return False
        if tipo_password not in opciones_pass:
            messagebox.showerror("Error", "El tipo de contraseña no es válido.")
            return False
        if len(tipo_password) > 15:
            messagebox.showerror("Error", "El tipo de contraseña no puede superar los 15 caracteres.")
            return False
        return True

    def validacion_password(self, password, tipo_password):
        if tipo_password in ["PIN", "Contraseña", "Patrón"]:
            if not password or password.strip() == "":
                messagebox.showerror("Error", "La contraseña es obligatoria.")
                return False
            if len(password) > 40:
                messagebox.showerror("Error", "La contraseña no puede superar los 40 caracteres.")
                return False
        
        return True


    def validacion_comentarios(self, comentarios):
        if len(comentarios) > 65535:
            messagebox.showerror("Error", "Los comentarios no pueden superar los 65535 caracteres.")
            return False
        
        return True

    def validacion_version(self, version):
        if not version or version.strip() == "":
            messagebox.showerror("Error", "El modelo es obligatorio.")
            return False
        if len(version) > 45:
            messagebox.showerror("Error", "El modelo no puede superar los 45 caracteres.")
            return False
        return True