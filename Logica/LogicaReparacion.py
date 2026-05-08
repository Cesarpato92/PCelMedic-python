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
        # Validar que el estado nuevo sea válido
        if modelo_reparacion.estado not in ["Completada", "Rechazada"]:
            return False, "El estado de la reparación no es válido."
        
        # Validar que el estado antiguo sea "En proceso"
        if estado_antiguo != "En proceso":
            return False, f"No se puede cambiar de estado {estado_antiguo}. Solo se pueden modificar reparaciones en estado 'En proceso'."
        
        # Validar comentarios del técnico (siempre requerido)
        if not modelo_reparacion.comentarios:
            return False, "El comentario del técnico es obligatorio."
        
        # Si es Completada, validar costo de repuestos
        if modelo_reparacion.estado == "Completada":
            if modelo_reparacion.costo_repuestos is None or modelo_reparacion.costo_repuestos < 0:
                return False, "El costo de repuestos debe ser un valor válido para reparaciones completadas."
            # Validar precio solo si es mayor a 0 (0 es valido cuando no se usaron repuestos)
            if modelo_reparacion.costo_repuestos > 0:
                res, msg = Validador.validar_precio(modelo_reparacion.costo_repuestos)
                if not res:
                    return False, msg
        
        # Si es Rechazada, el costo puede ser 0 o None
        elif modelo_reparacion.estado == "Rechazada":
            if modelo_reparacion.costo_repuestos is not None and modelo_reparacion.costo_repuestos < 0:
                return False, "El costo de repuestos no puede ser negativo."
            
        return True, ""

    def validacion_id_reparacion(self, id_reparacion):
        return Validador.validar_id(id_reparacion, "ID de reparación")
