from Utilidades.Validador import Validador
import DAO.ReparacionDAO as reparacion_dao

class LogicaReparacion:
    def __init__(self):
        self.reparacion_dao = reparacion_dao.ReparacionDAO()

    def agregar_reparacion(self, modelo_reparacion, cursor):
        valido, mensaje = self.validacion_datos_para_agregar(modelo_reparacion)
        if valido:
            return self.reparacion_dao.agregar_reparacion(modelo_reparacion, cursor)
        raise ValueError(mensaje)

    def actualizar_estado_reparacion(self, modelo_reparacion, estado_antiguo, cursor):
        valido, mensaje = self.validacion_datos_cambiar_estado(modelo_reparacion, estado_antiguo)
        if valido:
            return self.reparacion_dao.actualizar_estado_reparacion(modelo_reparacion, cursor)
        raise ValueError(mensaje)

    def obtener_reparacion_por_id(self, id_reparacion, cursor):
        valido, mensaje = self.validacion_id_reparacion(id_reparacion)
        if valido:
            return self.reparacion_dao.obtener_reparacion_por_id(id_reparacion, cursor)
        raise ValueError(mensaje)

    def validacion_datos_para_agregar(self, modelo_reparacion):
        if modelo_reparacion.precio_reparacion is None or modelo_reparacion.precio_reparacion <= 0:
            return False, "El precio de reparación debe ser mayor a 0."
        if modelo_reparacion.estado != "En proceso":
            return False, "La reparacion esta completada, no se puede agregar"
        return True, ""


    def validacion_datos_cambiar_estado(self, modelo_reparacion, estado_antiguo):
        res, msg = Validador.validar_precio(modelo_reparacion.costo_repuestos) if (modelo_reparacion.costo_repuestos is not None and modelo_reparacion.costo_repuestos != 0) else (True, "")
        if not res: return False, msg
            
        if modelo_reparacion.estado not in ["En Proceso", "Completada", "Entregada"]:
            return False, "El estado de la reparación no es válido."
        if estado_antiguo not in ["En Proceso", "Completada", "Entregada"]:
            return False, f"El estado {estado_antiguo} no es válido."
        if estado_antiguo == "Completada":
            return False, "Reparacion Completada no puede ser modificada"
        if not modelo_reparacion.comentarios:
            return False, "El comentario del técnico es obligatorio."
            
        return True, ""

    def validacion_id_reparacion(self, id_reparacion):
        return Validador.validar_id(id_reparacion, "ID de reparación")
