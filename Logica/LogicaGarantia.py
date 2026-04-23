from Utilidades.Validador import Validador

class LogicaGarantia:
    def __init__(self, garantia_dao):
        self.garantia_dao = garantia_dao

    def agregar_garantia(self, modelo_garantia, cursor=None):
        valido, mensaje = self.validar_campos_a_insertar(modelo_garantia)
        if valido:
            return self.garantia_dao.agregar_garantia(modelo_garantia, cursor)
        raise ValueError(mensaje)
    
    def obtener_garantia_por_id(self, id_garantia, cursor=None):
        valido, mensaje = self.validar_id(id_garantia)
        if valido:
            return self.garantia_dao.obtener_garantia_por_id(id_garantia, cursor)
        raise ValueError(mensaje)

    def actualizar_garantia(self, modelo_garantia, estado_antiguo,cursor=None):
        valido, mensaje = self.validar_campos_a_actualizar(modelo_garantia, estado_antiguo)
        if valido:
            return self.garantia_dao.actualizar_garantia(modelo_garantia, cursor)
        raise ValueError(mensaje)
    
    def validar_id(self, id_garantia):
        return Validador.validar_id(id_garantia, "ID de garantía")
    
    
    
    def validar_estado(self, estado, estado_antiguo):

        estados_validos = ["Completada", "En Garantia", "Rechazada"]
        if estado_antiguo not in ["Completada", "En Garantia", "Rechazada"]:
            return False, f"El estado '{estado_antiguo}' no es válido."
        if estado not in estados_validos:
            return False, f"El estado '{estado}' no es válido."
        if estado_antiguo != "En Garantia":
            return False, f"Garantía con estado '{estado_antiguo}' no puede modificarse, Agrega una nueva Garantia."
        return True, ""

    def validar_observaciones(self, observaciones):
        if not observaciones or observaciones.strip() == "":
            return False, "Las observaciones son obligatorias."
        return True, ""

    def validar_fecha_inicio(self, fecha_inicio):
        if not fecha_inicio:
            return False, "La fecha de inicio es obligatoria."
        return True, ""

    def validar_fecha_fin(self, fecha_fin):
        if not fecha_fin:
            return False, "La fecha de finalización es obligatoria."
        return True, ""

    def validar_precio_insumos(self, precio_insumos):
        return Validador.validar_precio(precio_insumos)

    def validar_comentarios_finales(self, comentarios_finales):
        if not comentarios_finales or comentarios_finales.strip() == "":
            return False, "Los comentarios finales son obligatorios."
        return True, ""

    def validar_campos_a_insertar(self, modelo_garantia):
        res, msg = self.validar_estado(modelo_garantia.estado)
        if not res: return False, msg
        res, msg = self.validar_observaciones(modelo_garantia.observaciones)
        if not res: return False, msg
        res, msg = self.validar_fecha_inicio(modelo_garantia.fecha_inicio)
        if not res: return False, msg
        return True, ""

    def validar_campos_a_actualizar(self, modelo_garantia, estado_antiguo):
        res, msg = self.validar_estado(modelo_garantia.estado, estado_antiguo)
        if not res: return False, msg
        res, msg = self.validar_fecha_fin(modelo_garantia.fecha_fin)
        if not res: return False, msg
        res, msg = self.validar_comentarios_finales(modelo_garantia.comentarios_finales)
        if not res: return False, msg
        return True, ""
