from Utilidades.Validador import Validador
import DAO.DispositivoDAO as dispositivo_dao

class LogicaDispositivo:
    def __init__(self):
        self.dispositivo_dao = dispositivo_dao.DispositivoDAO()
        
    def agregar_dispositivo(self, modelo_dispositivo, cursor):
        valido, mensaje = self.validacion_datos(modelo_dispositivo)
        if valido:
            return self.dispositivo_dao.agregar_dispositivo(modelo_dispositivo, cursor)
        raise ValueError(mensaje)

    def obtener_dispositivo_por_id(self, id_disp, cursor):
        valido, mensaje = self.validacion_id_dispositivo(id_disp)
        if valido:
            return self.dispositivo_dao.obtener_dispositivo_por_id(id_disp, cursor)
        raise ValueError(mensaje)
    
    def actualizar_dispositivo(self, modelo_dispositivo, cursor):
        self.dispositivo_dao.actualizar_dispositivo(modelo_dispositivo, cursor)
    
    def validacion_datos(self, modelo_dispositivo):
        res, msg = self.validacion_marca(modelo_dispositivo.marca)
        if not res: return False, msg
        
        res, msg = self.validacion_tipo_reparacion(modelo_dispositivo.tipo_reparacion)
        if not res: return False, msg
        
        res, msg = self.validacion_tipo_password(modelo_dispositivo.tipo_password)
        if not res: return False, msg
        
        res, msg = self.validacion_password(modelo_dispositivo.password, modelo_dispositivo.tipo_password)
        if not res: return False, msg
        
        res, msg = self.validacion_comentarios(modelo_dispositivo.comentarios)
        if not res: return False, msg
        
        res, msg = self.validacion_version(modelo_dispositivo.version)
        if not res: return False, msg
        
        return True, ""
    
    def validacion_id_dispositivo(self, id_disp):
        return Validador.validar_id(id_disp, "ID del dispositivo")

    def validacion_marca(self, marca):
        if not marca or marca.strip() == "":
            return False, "La marca es obligatoria."
        if len(marca) > 45:
            return False, "La marca no puede superar los 45 caracteres."
        return True, ""

    def validacion_tipo_reparacion(self, tipo_reparacion):
        opciones_rep = ["Display", "Puerto de carga", "Corto", "Sonido", "Cuenta", "Bloqueo", "Otro"]
        if not tipo_reparacion or tipo_reparacion.strip() == "":
            return False, "El tipo de reparación es obligatorio."
        if tipo_reparacion not in opciones_rep:
            return False, "El tipo de reparación no es válido."
        if len(tipo_reparacion) > 100:
            return False, "El tipo de reparación no puede superar los 100 caracteres."
        return True, ""

    def validacion_tipo_password(self, tipo_password):
        # Sincronizado con GUI: "Patrón", "Texto/Números", "PIN", "Sin contraseña"
        opciones_pass = ["PIN", "Texto/Números", "Patrón", "Sin contraseña"]
        if not tipo_password or tipo_password.strip() == "":
            return False, "El tipo de contraseña es obligatorio."
        if tipo_password not in opciones_pass:
            return False, f"El tipo de contraseña '{tipo_password}' no es válido."
        return True, ""

    def validacion_password(self, password, tipo_password):
        if tipo_password in ["PIN", "Texto/Números", "Patrón"]:
            if not password or password.strip() == "":
                return False, "La contraseña es obligatoria."
            if len(password) > 40:
                return False, "La contraseña no puede superar los 40 caracteres."
        return True, ""

    def validacion_comentarios(self, comentarios):
        if comentarios and len(comentarios) > 65535:
            return False, "Los comentarios no pueden superar los 65535 caracteres."
        return True, ""

    def validacion_version(self, version):
        if not version or version.strip() == "":
            return False, "El modelo es obligatorio."
        if len(version) > 45:
            return False, "El modelo no puede superar los 45 caracteres."
        return True, ""